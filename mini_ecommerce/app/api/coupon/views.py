from fastapi import APIRouter, status
from typing import List
from fastapi import Depends
from app.models.models import Coupon
from mini_ecommerce.app.models.models import Coupon
from .schemas import ProductDiscountSchema
from .schemas import ShowProductDiscountSchema
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.repositories.coupon_repository import CouponRepository

from app.services.coupon_service import CouponService
from .schemas import CouponSchema

router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(coupon: CouponSchema, service: CouponService = Depends()):
    service.create_coupon(coupon)
   

# @router.get('/', response_model=List[ShowCoupontSchema])
# def index(repository: ProductDiscountRepository = Depends()):
#     return repository.get_all()
    

# @router.put(' /{id}')
# def update(id: int, productDiscount: ProductDiscountSchema,repository: ProductDiscountRepository = Depends()):
#    repository.update(id, productDiscount.dict())

# @router.get('/{id}', response_model = ShowProductDiscountSchema)
# def show(id: int, repository: ProductDiscountRepository = Depends()):
#     return repository.get_by_id(id)