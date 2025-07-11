from . import db
from . import models, crud, schemas

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

@app.post("/users/", response_model=schemas.User)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user_in)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(404, detail="User not found")
    return db_user


# ------ Categorias ------

@app.post("/categories/", response_model=schemas.Category)
def create_category(cat_in: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, cat_in)

@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip, limit)


# ------ Transações ------

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(tx_in: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, tx_in)

@app.get("/transactions/", response_model=list[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_transactions(db, skip, limit)

@app.get("/transactions/{tx_id}", response_model=schemas.Transaction)
def read_transaction(tx_id: int, db: Session = Depends(get_db)):
    db_tx = crud.get_transaction(db, tx_id)
    if not db_tx:
        raise HTTPException(404, detail="Transaction not found")
    return db_tx
