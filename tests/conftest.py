# tests/conftest.py

import sys, os
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
)

import pytest

from sqlalchemy      import create_engine
from sqlalchemy.orm  import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app.db     import Base
from backend.app.main   import app, get_db
from fastapi.testclient import TestClient

# 1) Engine e Session para SQLite :memory:
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,           # <— força reuse da mesma conexão
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2) Fixture que fornece uma sessão de DB
@pytest.fixture(scope="function")
def db_session():
    # Limpa e (re)cria as tabelas num banco em memória
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# 3) Override da dependência get_db do FastAPI
@pytest.fixture(scope="function")
def client(db_session):
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    return TestClient(app)
