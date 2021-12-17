from fastapi import Depends
from app.repositories.payment_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.productDiscount.schemas import ProductDiscountSchema
from app.common.exceptions import ProductDiscountIdAlreadyExistsException
from app.common.exceptions import ProductDiscountIdNotExistsException

from app.models.models import Payment


class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(), 
                product_discount_repository: ProductDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, productDiscount: ProductDiscountSchema):
        find_by_id = self.product_discount_repository.find_by_id(productDiscount.id)
        if find_by_id:
            raise ProductDiscountIdAlreadyExistsException()

        self.product_discount_repository.create(ProductDiscountSchema(**productDiscount.dict()))
    
    def update_productDiscount(self, productDiscount: ProductDiscountSchema):
        find_by_id = self.product_discount_repository.find_by_id(productDiscount.id)

        if find_by_id:
            self.product_discount_repository.update(ProductDiscountSchema(**productDiscount.dict()))

        raise ProductDiscountIdNotExistsException()
            