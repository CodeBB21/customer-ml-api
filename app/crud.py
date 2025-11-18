from sqlalchemy.orm import Session
from . import models, schemas


# -----------------------
# CUSTOMERS
# -----------------------

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers(db: Session):
    return db.query(models.Customer).all()


# -----------------------
# TRANSACTIONS
# -----------------------

def create_transaction(db: Session, tx: schemas.TransactionCreate):
    db_tx = models.Transaction(
        customer_id=tx.customer_id,
        amount=tx.amount,
        category=tx.category
    )
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx


def get_transactions(db: Session, customer_id: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.customer_id == customer_id)
        .all()
    )
