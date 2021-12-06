from fastapi import Depends
from app.repositories.payment_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.repositories.coupon_repository import CouponRepository

from app.api.coupon.schemas import CouponSchema


class CouponService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 coupon_repository: CouponRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.coupon_repository = coupon_repository

    def create_coupon(self, coupon: CouponSchema):
        pass