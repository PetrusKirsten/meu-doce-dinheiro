# backend/app/main.py

from . import db
from . import models, crud, schemas

from .schemas import MonthlyBalance

from sqlalchemy.orm          import Session
from fastapi                 import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Meu Doce Dinheiro API")

# ===== CORS (para consumo pelo frontend em http://localhost:3000) =====
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],  # endereço do Next.js local
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Garante que as tabelas existam
models.Base.metadata.create_all(bind=db.engine)

# Dependência para obter a sessão do banco
def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()


# ------ Usuários ------

# Create a new user
@app.post("/users/", response_model=schemas.User)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user_in)

# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

# Get user by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(404, detail="User not found")
    return db_user

# Update user by ID
@app.put("/users/{user_id}",
         response_model=schemas.User,
         tags=["users"])

def api_update_user(
    user_id : int,
    user_in : schemas.UserUpdate,
    db      : Session = Depends(get_db)):

    return crud.update_user(db, user_id, user_in)

# Delete user by ID
@app.delete("/users/{user_id}",
            status_code=204,
            tags=["users"])

def api_delete_user(
    user_id : int,
    db      : Session = Depends(get_db)):

    crud.delete_user(db, user_id)
    
    return


# ------ Categorias ------

# Get category by ID
@app.post("/categories/", response_model=schemas.Category)
def create_category(cat_in: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, cat_in)

# Get all categories
@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip, limit)

# Get category by ID
@app.put("/categories/{cat_id}",
         response_model=schemas.Category,
         tags=["categories"])

def api_update_category(
    cat_id : int,
    cat_in : schemas.CategoryUpdate,
    db     : Session = Depends(get_db)):

    return crud.update_category(db, cat_id, cat_in)

# Delete category by ID
@app.delete("/categories/{cat_id}",
            status_code=204,
            tags=["categories"])

def api_delete_category(
    cat_id : int,
    db     : Session = Depends(get_db)):

    crud.delete_category(db, cat_id)
    return


# ------ Transações ------

# Create a new transaction
@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(tx_in: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, tx_in)

# Get all transactions
@app.get("/transactions/", response_model=list[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db)

# Get transaction by ID
@app.get("/transactions/{tx_id}", response_model=schemas.Transaction)
def read_transaction(tx_id: int, db: Session = Depends(get_db)):
    db_tx = crud.get_transaction(db, tx_id)
    if not db_tx:
        raise HTTPException(404, detail="Transaction not found")
    return db_tx

# Update transaction by ID
@app.put("/transactions/{tx_id}",
         response_model=schemas.Transaction,
         tags=["transactions"])

def api_update_transaction(
    tx_id : int,
    tx_in : schemas.TransactionUpdate,
    db    : Session = Depends(get_db)):

    return crud.update_transaction(db, tx_id, tx_in)

# Delete transaction by ID
@app.delete("/transactions/{tx_id}",
            status_code=204,
            tags=["transactions"])

def api_delete_transaction(
    tx_id : int,
    db    : Session = Depends(get_db)):

    crud.delete_transaction(db, tx_id)
    return


# ------ Relatórios ------

@app.get("/reports/monthly-balance/{year}",
         response_model=list[MonthlyBalance],
         tags=["reports"])

def read_monthly_balance(year: int, db: Session = Depends(get_db)):
    return crud.get_monthly_balance(db, year)
