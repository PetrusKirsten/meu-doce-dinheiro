# tests/test_main.py
from http import HTTPStatus

def test_create_and_read_user(client):
    # POST /users/
    resp = client.post("/users/", json={
        "name"     : "Carol",
        "email"    : "carol@example.com",
        "password" : "123"})
    
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert data["id"] == 1 and data["name"] == "Carol"

    # GET /users/1
    resp2 = client.get("/users/1")
    assert resp2.status_code == HTTPStatus.OK
    assert resp2.json()["email"] == "carol@example.com"

def test_list_categories_empty(client):
    resp = client.get("/categories/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == []

def test_endpoints_transactions(client):
    # Cria user e categoria
    client.post("/users/", json={"name":"X","email":"x@y","password":"p"})
    client.post("/categories/", json={"name":"Test"})
    # Cria transação
    resp = client.post("/transactions/", json={
        "amount"      : 50.0,
        "date"        : "2025-07-11T00:00:00",
        "description" : "Teste",
        "category_id" : 1,
        "owner_id"    : 1})
    
    assert resp.status_code == HTTPStatus.OK
    tx = resp.json()
    assert tx["amount"] == 50.0

    # Lista
    list_resp = client.get("/transactions/")
    assert list_resp.status_code == HTTPStatus.OK
    assert len(list_resp.json()) == 1
