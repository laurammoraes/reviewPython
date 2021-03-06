from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import ProductDiscount
from mini_ecommerce.app.db.db import Base
from .base_repository import BaseRepository


class ProductDiscountRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, ProductDiscount)

    def find_by_id(self, id):
        return self.session.query(self.model).filter_by(id=id).first()