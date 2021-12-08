from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import Admin
from .schemas import AdminSchema
from .schemas import ShowAdminSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.repositories.admin_repository import AdminRepository
from app.services.admin_service import AdminService

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(admin: AdminSchema, service: AdminService = Depends()):
    repository.create(Admin(**admin.dict()))

@router.get('/', response_model=List[ShowAdminSchema])
def index(repository: AdminRepository = Depends()):
    return repository.get_all()
    

@router.put(' /{id}')
def update(id: int, admin: AdminSchema, repository: AdminRepository = Depends()):
    repository.update(id, admin.dict())

@router.get('/{id}', response_model = ShowAdminSchema)
def show(id: int, repository: AdminRepository = Depends()):
    return repository.get_by_id(id)