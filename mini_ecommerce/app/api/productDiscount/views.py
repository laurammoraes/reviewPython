from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import ProductDiscount
from app.models.models import Product
from .schemas import ProductDiscountSchema

from sqlalchemy.orm import Session
from app.db.db import get_db
from app.repositories.product_discount_repository import ProductDiscountRepository

from app.services.product_discount_service import ProductDiscountService
from .schemas import ProductDiscountSchema

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(productDiscount: ProductDiscountSchema, service: ProductDiscountService = Depends()):
    service.create_discount(productDiscount)
   

@router.get('/')
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, repository: ProductDiscountRepository = Depends()):
    repository.remove(id)