from fastapi import Depends
from app.repositories.payment_repository import PaymentMethodRepository

from app.repositories.coupon_repository import CouponRepository

from app.api.coupon.schemas import CouponSchema
from app.api.coupon.schemas import CouponUpdateSchema
from app.common.exceptions import CouponCodeAlreadyExistsException
from app.api.coupon.schemas import CouponType
from app.common.exceptions import CouponCodeNotExistsException


class CouponService:
    def __init__(self, coupon_repository: CouponRepository = Depends()):
        self.coupon_repository = coupon_repository
       
    def create_coupon(self, coupon: CouponSchema):
        find_by_code = self.coupon_repository.find_by_code(coupon.code)
        if find_by_code:
                raise CouponCodeAlreadyExistsException()

        self.coupon_repository.create(CouponType(**coupon.dict()))

    def update_coupon(self, coupon: CouponUpdateSchema):
        find_by_code = self.coupon_repository.find_by_code(coupon.code)

        if find_by_code:
            self.coupon_repository.update(CouponUpdateSchema(**coupon.dict()))

        raise CouponCodeNotExistsException()
        