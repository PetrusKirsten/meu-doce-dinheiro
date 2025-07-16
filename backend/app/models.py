from .db import Base  # importando o declarative_base do db.py

from datetime       import datetime
from sqlalchemy.orm import relationship
from sqlalchemy     import Column, Integer, Float, DateTime, String, ForeignKey, Boolean

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String,  unique=True,      index=True)
    email           = Column(String,  unique=True,      index=True)
    onboarded       = Column(Boolean, default=False, nullable=False) 

    # Relacionamento para transações que esse usuário possui
    transactions = relationship("Transaction", back_populates="owner")


class Category(Base):
    __tablename__ = "categories"

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String,  unique=True,      index=True)

    # Relacionamento com transações dessa categoria
    transactions = relationship("Transaction", back_populates="category")


class Transaction(Base):
    __tablename__ = "transactions"

    id          = Column(Integer,  primary_key=True, index=True)
    amount      = Column(Float,    nullable=False)
    date        = Column(DateTime, default=datetime.utcnow, index=True)
    description = Column(String,   nullable=True)

    # Chaves estrangeiras
    owner_id    = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relacionamentos
    owner    = relationship("User",     back_populates="transactions")
    category = relationship("Category", back_populates="transactions")

