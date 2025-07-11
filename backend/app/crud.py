from . import models, schemas

from sqlalchemy     import func
from sqlalchemy.orm import Session


# ------ Usuários ------

def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user_in: schemas.UserCreate) -> models.User:
    db_user = models.User(name=user_in.name, email=user_in.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# ------ Categorias ------

def get_category(db: Session, category_id: int) -> models.Category | None:
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100) -> list[models.Category]:
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, cat_in: schemas.CategoryCreate) -> models.Category:
    db_cat = models.Category(name=cat_in.name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)

    return db_cat


# ------ Transações ------

def get_transaction(db: Session, tx_id: int) -> models.Transaction | None:
    return db.query(models.Transaction).filter(models.Transaction.id == tx_id).first()

def get_transactions(
    db    : Session,
    skip  : int = 0,
    limit : int = 100) -> list[models.Transaction]:
    
    return db.query(models.Transaction).offset(skip).limit(limit).all()

def create_transaction(
    db    : Session,
    tx_in : schemas.TransactionCreate) -> models.Transaction:
    
    db_tx = models.Transaction(
        amount      = tx_in.amount,
        date        = tx_in.date,
        description = tx_in.description,
        owner_id    = tx_in.owner_id,
        category_id = tx_in.category_id)
    
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)

    return db_tx

# (Opcional) funções de atualização e remoção seguem padrão similar:
# def update_transaction(...), def delete_transaction(...)


# ------ Relatórios ------

def get_monthly_balance(db: Session, year: int) -> list[dict]:
    """
    Retorna lista de { month: 'YYYY-MM', balance: total_receitas - total_despesas } 
    para cada mês do ano informado.
    """
    # Formata '2025-07-11' como '2025-07'
    month_col = func.strftime("%Y-%m", models.Transaction.date)

    # Soma receitas e despesas por mês
    results = (
        db.query(
            month_col.label("month"),
            (func.sum(
                func.case(
                    [
                        (models.Transaction.amount >= 0, models.Transaction.amount),
                        (models.Transaction.amount < 0, models.Transaction.amount)
                    ]
                )
            )).label("balance")
        )
        .filter(func.strftime("%Y", models.Transaction.date) == str(year))
        .group_by(month_col)
        .order_by(month_col)
        .all()
    )
    # results virá como lista de tuples; converte em list[dict]
    return [ {"month": m, "balance": b} for m, b in results ]
