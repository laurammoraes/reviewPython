from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DATETIME, VARCHAR, Boolean, Date, Float, Integer, String 
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

class Coupon(Base): 
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key= True )
    code = Column(VARCHAR(10))
    expire_at = Column(DATETIME)
    limit = Column(Integer)
    type = Column(VARCHAR(15))
    value = Column(Float)

class User(Base): 
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True )
    displayname = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    role = Column(VARCHAR(45))
    password = Column(VARCHAR(45))
    

class Customer(Base): 
    __tablename__ = 'customers'

    id = Column(Integer, primary_key= True )
    firstName = Column(VARCHAR(45))
    lastName = Column(VARCHAR(45))
    phoneNumber = Column(VARCHAR(45))
    genre = Column(VARCHAR(45))
    documentId = Column(VARCHAR(45))
    birthDate = Column(Date)

class Adress(Base):
    __tablename__= 'address'

    id = Column(Integer, primary_key= True)
    address = Column(VARCHAR(45))
    city = Column(VARCHAR(45))
    state = Column(VARCHAR(45))
    number = Column(VARCHAR(10))
    zipcode = Column(VARCHAR(6))
    neighbourhood = Column(VARCHAR(45))
    primary = Column(Integer)  
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customer)  
    



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