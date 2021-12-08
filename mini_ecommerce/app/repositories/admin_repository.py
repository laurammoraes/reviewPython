from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Admin
from .base_repository import BaseRepository


class AdminRepository:
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Admin)

   