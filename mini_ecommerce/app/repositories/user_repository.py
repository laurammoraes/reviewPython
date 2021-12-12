from sqlalchemy.orm.session import Session
from .base_repository import BaseRepository
from sqlalchemy.orm import Session

class UserRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, User)

    def find_by_email(self, email):
        
        return self.session.query(self.model).filter_by(email=email).first()

