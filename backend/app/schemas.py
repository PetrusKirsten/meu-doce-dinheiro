from pydantic import BaseModel
from datetime import datetime


# -------------------------
# Schemas para User
# -------------------------
class UserBase(BaseModel):
    name  : str
    email : str

class UserCreate(UserBase):
    password : str  # se você tiver autenticação, ou remova este campo

class User(UserBase):
    id : int

    class Config:
        rom_attributes = True


# -------------------------
# Schemas para Category
# -------------------------
class CategoryBase(BaseModel):
    name : str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id : int

    class Config:
        rom_attributes = True


# -------------------------
# Schemas para Transaction
# -------------------------
class TransactionBase(BaseModel):
    amount      : float
    date        : datetime
    description : str | None = None
    category_id : int
    owner_id    : int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id : int

    class Config:
        rom_attributes = True
