from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String 
from app.db.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)

class Category(Base):
    __tablename__='categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))


class Suplier(Base):
    __tablename__= 'supliers'

    id = Column(Integer, primary_key = True)
    name = Column(String(150))
    
class Payment(Base):
    __tablename__='payments'

    id = Column(Integer, primary_key = True)
    name = Column(String(150))
    enabled = Column(Integer)