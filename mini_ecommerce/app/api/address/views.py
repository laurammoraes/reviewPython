from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from .schemas import AdressesSchema 
from .schemas import ShowAdressesSchema
from app.repositories.adress_repository import AdressRepository
from app.models.models import Adress
from sqlalchemy.orm import Session
from app.db.db import get_db


router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(adress: AdressesSchema, repository: AdressRepository = Depends()):
   repository.create(Adress(**adress.dict()))

@router.get('/', response_model=List[ShowAdressesSchema])
def index(repository: AdressRepository = Depends()):
    return repository.get_all()
    

@router.put(' /{id}')
def update(id: int, adress:AdressesSchema, repository: AdressRepository = Depends()):
     repository.update(id, adress.dict())

@router.get('/{id}', response_model = AdressesSchema)
def show(id: int,  repository: AdressRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, repository: AdressRepository = Depends()):
    repository.remove(id)