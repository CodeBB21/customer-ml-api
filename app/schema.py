from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


# -----------------
# CUSTOMERS
# -----------------

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # important pour SQLAlchemy


# -----------------
# TRANSACTIONS
# -----------------

class TransactionBase(BaseModel):
    amount: float
    category: str


class TransactionCreate(TransactionBase):
    customer_id: int


class TransactionRead(TransactionBase):
    id: int
    customer_id: int
    timestamp: datetime

    class Config:
        from_attributes = True
