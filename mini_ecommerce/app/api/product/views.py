from fastapi import APIRouter, status
from typing import List
from fastapi import Depends

from app.models.models import Product

from .schemas import ProductSchema
from .schemas import ShowProductSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.repositories.product_repository import ProductRepository

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(product: ProductSchema, repository: ProductRepository = Depends()):
   repository.create(Product(**product.dict()))

@router.get('/', response_model=List[ShowProductSchema])
def index(repository: ProductRepository = Depends()):
    return repository.get_all()
    

@router.put(' /{id}')
def update(id: int, product: ProductSchema, repository: ProductRepository = Depends()):
   repository.update(id, product.dict())

@router.get('/{id}', response_model = ShowProductSchema)
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)