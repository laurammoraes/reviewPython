from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import ProductDiscount
from mini_ecommerce.app.models.models import Product
from .schemas import ProductDiscountSchema
from .schemas import ShowProductDiscountSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.repositories.product_discount_repository import ProductDiscountRepository

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(productDiscount: ProductDiscountSchema, repository: ProductDiscountRepository = Depends()):
    repository.create(Product(**productDiscount.dict()))
   

@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()
    

@router.put(' /{id}')
def update(id: int, productDiscount: ProductDiscountSchema,repository: ProductDiscountRepository = Depends()):
   repository.update(id, productDiscount.dict())

@router.get('/{id}', response_model = ShowProductDiscountSchema)
def show(id: int, repository: ProductDiscountRepository = Depends()):
    return repository.get_by_id(id)