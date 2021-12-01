from fastapi import APIRouter
from .product.views import router as product_router
from .category.views import router as category_router
from .suplier.views import router as suplier_router
from .payment.views import router as payment_router



router = APIRouter()

router.include_router(product_router, prefix= '/product')
router.include_router(category_router, prefix= '/category')
router.include_router(suplier_router, prefix= '/suplier')
router.include_router(payment_router, prefix= '/payment')


