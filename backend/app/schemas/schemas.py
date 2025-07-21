from datetime import datetime
from pydantic import BaseModel, ConfigDict

# -------------------------
# Schemas para User
# -------------------------

class LoginIn(BaseModel):
    email    : str
    password : str

class TokenOut(BaseModel):
    access_token : str
    token_type   : str = "bearer"

class UserBase(BaseModel):
    name  : str
    email : str

class UserCreate(UserBase):
    name     : str
    email    : str
    password : str

class UserUpdate(BaseModel):
    name  : str | None = None
    email : str | None = None

    model_config = ConfigDict(from_attributes=True)

class User(UserBase):
    id              : int
    name            : str
    email           : str
    hashed_password : str 
    onboarded       : bool

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Schemas para Category
# -------------------------
class CategoryBase(BaseModel):
    name : str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id : int

    model_config = ConfigDict(from_attributes=True)

class CategoryUpdate(BaseModel):
    name: str | None = None

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)

class TransactionUpdate(BaseModel):
    amount      : float | None = None
    date        : str   | None = None
    description : str   | None = None
    category_id : int   | None = None
    owner_id    : int   | None = None

    model_config = ConfigDict(from_attributes=True)


# -------------------------
# Schemas para relatórios
# -------------------------
class MonthlyBalance(BaseModel):
    month   : str    # ex. "2025-01"
    balance : float

    model_config = ConfigDict(from_attributes=True)

