from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/", response_model=schemas.TransactionRead)
def create_transaction(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, tx)


@router.get("/{customer_id}", response_model=list[schemas.TransactionRead])
def get_transactions(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions(db, customer_id)
