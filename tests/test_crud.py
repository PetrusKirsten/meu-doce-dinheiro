# tests/test_crud.py
import pytest

from backend.app import crud, models, schemas

def test_create_and_get_user(db_session):
    # 1) Cria um usuário
    user_in = schemas.UserCreate(name="Bob", email="bob@example.com", password="x")
    db_user = crud.create_user(db_session, user_in)

    assert db_user.id is not None
    assert db_user.name == "Bob"

    # 2) Busca pelo mesmo usuário
    fetched = crud.get_user(db_session, db_user.id)
    assert fetched.email == "bob@example.com"

def test_create_category_and_list(db_session):
    cat_in = schemas.CategoryCreate(name="Lazer")
    db_cat = crud.create_category(db_session, cat_in)
    assert db_cat.id and db_cat.name == "Lazer"

    all_cats = crud.get_categories(db_session)
    assert len(all_cats) == 1
    assert all_cats[0].name == "Lazer"

def test_create_transaction(db_session):
    # Primeiro cria user e category
    user  = crud.create_user(db_session, schemas.UserCreate(name="T", email="t@x", password="x"))
    cat   = crud.create_category(db_session, schemas.CategoryCreate(name="Teste"))
    tx_in = schemas.TransactionCreate(
        amount      = 100.0,
        date        = "2025-07-11T00:00:00",
        description = "Compra",
        category_id = cat.id,
        owner_id    = user.id
    )
    tx = crud.create_transaction(db_session, tx_in)
    assert tx.id and tx.amount == 100.0
    assert tx.owner_id == user.id
