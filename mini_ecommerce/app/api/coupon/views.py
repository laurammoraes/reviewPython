from fastapi import APIRouter, status
from typing import List
from fastapi import Depends

from app.models.models import Coupon
from app.repositories.coupon_repository import CouponRepository


from app.db.db import get_db
from app.repositories.coupon_repository import CouponRepository

from app.services.coupon_service import CouponService
from .schemas import CouponSchema
from .schemas import CouponUpdateSchema


router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(coupon: CouponSchema, service: CouponService = Depends()):
    service.create_coupon(coupon)
   

@router.get('/')
def index(repository: CouponRepository = Depends()):
    return repository.get_all()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, repository: CouponRepository = Depends()):
    repository.remove(id)

@router.put('/{id}', status_code= status.HTTP_201_CREATED)
def create(coupon: CouponUpdateSchema, service: CouponService = Depends()):
    service.update_coupon(coupon)
