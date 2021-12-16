from fastapi import APIRouter
from fastapi.param_functions import Depends
from app.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/')
def create(repository: UserRepository = Depends())
    repository.create()