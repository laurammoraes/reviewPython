
from fastapi import Depends
from app.repositories.payment_repository import PaymentMethodRepository


class ProductDiscountService:
    def __init__(self, repository) -> None:
        pass