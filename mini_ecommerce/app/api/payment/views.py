from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import Payment
from .schemas import PaymentSchema
from .schemas import ShowPaymentSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(payment: PaymentSchema, db: Session = Depends(get_db)):
    db.add(Payment(**payment.dict()))
    db.commit()

@router.get('/', response_model=List[ShowPaymentSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Payment).all()
    

@router.put(' /{id}')
def update(id: int, payment: PaymentSchema, db: Session = Depends(get_db)):
    query = db.query(Payment).filter_by(id=id)   
    query.update(payment.dict())
    db.commit()

@router.get('/{id}', response_model = ShowPaymentSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Payment).filter_by(id=id).first()