from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String 
from app.db.db import Base


class Category(Base):
    __tablename__='categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))


class Supplier(Base):
    __tablename__= 'suppliers'

    id = Column(Integer, primary_key = True)
    name = Column(String(150))
    
class Payment(Base):
    __tablename__='payments'

    id = Column(Integer, primary_key = True)
    name = Column(String(150))
    enabled = Column(Integer)






class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10,2))
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship(Supplier)


class ProductDiscount(Base):
    __tablename__='productDiscounts'

    id = Column(Integer, primary_key= True)
    mode = Column(String(255))
    value = Column(Float(10,2))
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)
    payment_method_id = Column(Integer, ForeignKey('payments.id'))
    payment = relationship(Payment)