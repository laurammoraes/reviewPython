from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import Suplier
from .schemas import SuplierSchema
from .schemas import ShowSuplierSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(suplier: SuplierSchema, db: Session = Depends(get_db)):
    db.add(Suplier(**suplier.dict()))
    db.commit()

@router.get('/', response_model=List[ShowSuplierSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Suplier).all()
    

@router.put(' /{id}')
def update(id: int, suplier: SuplierSchema, db: Session = Depends(get_db)):
    query = db.query(Suplier).filter_by(id=id)   
    query.update(suplier.dict())
    db.commit()

@router.get('/{id}', response_model = ShowSuplierSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Suplier).filter_by(id=id).first()