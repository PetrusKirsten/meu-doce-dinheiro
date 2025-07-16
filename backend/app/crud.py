from . import models, schemas

from fastapi import HTTPException, status

from sqlalchemy     import func
from sqlalchemy.orm import Session


# ------ Usuários ------

def get_user(db      : Session, 
             user_id : int) -> models.User | None:
    
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db    : Session,
              skip  : int = 0, 
              limit : int = 100) -> list[models.User]:
    
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db      : Session,
                user_in : schemas.UserCreate) -> models.User:
    
    db_user = models.User(name=user_in.name, email=user_in.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def update_user(db      : Session,
                user_id : int,
                data    : schemas.UserUpdate) -> models.User:
    """ Atualiza um usuário existente com os dados fornecidos. """

    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = data.model_dump(exclude_none=True)

    for key, val in update_data.items():
        setattr(user, key, val)

    db.commit()
    db.refresh(user)

    return user

def delete_user(db      : Session,
                user_id : int) -> None:

    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()


def mark_user_onboarded(db      : Session, 
                        user_id : int) -> models.User:
    
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado")
    
    user.onboarded = True
    
    db.commit()
    db.refresh(user)

    return user

# ------ Categorias ------

def get_category(db          : Session, 
                 category_id : int) -> models.Category | None:
    
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db    : Session, 
                   skip  : int = 0, 
                   limit : int = 100) -> list[models.Category]:
    
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db     : Session, 
                    cat_in : schemas.CategoryCreate) -> models.Category:
    
    db_cat = models.Category(name=cat_in.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)

    return db_cat

def update_category(db     : Session, 
                    cat_id : int, 
                    data   : schemas.CategoryUpdate) -> models.Category:

    cat = db.get(models.Category, cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = data.model_dump(exclude_none=True)
    
    for key, val in update_data.items():
        setattr(cat, key, val)

    db.commit()
    db.refresh(cat)
    
    return cat

def delete_category(db     : Session, 
                    cat_id : int) -> None:
    # Verifica se existe alguma transação usando essa categoria
    in_use = (
        db.query(models.Transaction)
          .filter(models.Transaction.category_id == cat_id)
          .count())    
    if in_use:
        raise HTTPException(status_code = 400,
                            detail      = "Não é possível deletar categoria que possui transações.")

    cat = db.get(models.Category, cat_id)
    if not cat:
        raise HTTPException(status_code = 404,
                            detail      = "Categoria não encontrada.")

    db.delete(cat)
    db.commit()


# ------ Transações ------

def get_transaction(db    : Session, 
                    tx_id : int) -> models.Transaction | None:
    
    return db.query(models.Transaction).filter(models.Transaction.id == tx_id).first()

def get_transactions(db: Session) -> list[models.Transaction]:
    """
    Retorna apenas transações que ainda têm categoria e usuário válidos.
    """
    
    return (
        db.query(models.Transaction)
          .filter(models.Transaction.category_id != None)   # exclui None
          .filter(models.Transaction.owner_id    != None)   # só pra garantir
          .all()
    )

def create_transaction(db      : Session,
                       tx_in   : schemas.TransactionCreate,
                       user_id : int,) -> models.Transaction:
    
    db_tx = models.Transaction(
        amount      = tx_in.amount,
        date        = tx_in.date,
        description = tx_in.description,
        owner_id    = user_id,
        category_id = tx_in.category_id)
    
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)

    return db_tx

def update_transaction(db    : Session, 
                       tx_id : int, 
                       data  : schemas.TransactionUpdate) -> models.Transaction:
    
    tx = db.get(models.Transaction, tx_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    update_data = data.model_dump(exclude_none=True)
    
    for key, val in update_data.items():
        setattr(tx, key, val)
    
    db.commit()
    db.refresh(tx)
    
    return tx

def delete_transaction(db    : Session, 
                       tx_id : int) -> None:
    
    tx = db.get(models.Transaction, tx_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    db.delete(tx)
    db.commit()

# (Opcional) funções de atualização e remoção seguem padrão similar:
# def update_transaction(...), def delete_transaction(...)


# ------ Relatórios ------

def get_monthly_balance(db   : Session, 
                        year : int) -> list[dict]:
    """
    Retorna lista de { month: 'YYYY-MM', balance: total_receitas - total_despesas }
    para cada mês do ano informado.
    """
    # Coluna com 'YYYY-MM' extraída da data
    
    month_col = func.strftime("%Y-%m", models.Transaction.date)

    # Soma simples do campo amount por mês
    results = (
        db.query(
            month_col.label("month"),
            func.sum(models.Transaction.amount).label("balance")
        )
        .filter(func.strftime("%Y", models.Transaction.date) == str(year))
        .group_by(month_col)
        .order_by(month_col)
        .all()
    )

    # Converte cada tupla (month, balance) em dict
    return [{"month": m, "balance": b} for m, b in results]
