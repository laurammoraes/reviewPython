from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import Payment
from .schemas import PaymentSchema
from .schemas import ShowPaymentSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.repositories.payment_repository import PaymentMethodRepository

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(payment: PaymentSchema, repository: PaymentMethodRepository = Depends()):
   repository.create(Payment(**payment.dict()))

@router.get('/', response_model=List[ShowPaymentSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()
        

@router.put(' /{id}')
def update(id: int, payment: PaymentSchema, repository: PaymentMethodRepository = Depends()):
     repository.update(id, payment.dict())

@router.get('/{id}', response_model = ShowPaymentSchema)
def show(id: int,  repository: PaymentMethodRepository = Depends()):
    return repository.get_by_id(id)