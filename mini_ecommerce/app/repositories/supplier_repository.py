from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Supplier
from mini_ecommerce.app.db.db import Base
from .base_repository import BaseRepository


class SupplierRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Supplier)
    def find_by_id(self, id):
        return self.session.query(self.model).filter_by(id=id).first()
        

  