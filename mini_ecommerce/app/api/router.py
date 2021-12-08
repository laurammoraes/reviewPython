from fastapi import APIRouter
from .product.views import router as product_router
from .category.views import router as category_router
from .supplier.views import router as supplier_router
from .payment.views import router as payment_router
from .productDiscount.views import router as productDiscount_router
from .coupon.views import router as coupon_router
from .customer.views import router as customer_router
from .address.views import router as address_router






router = APIRouter()

router.include_router(product_router, prefix= '/product')
router.include_router(category_router, prefix= '/category')
router.include_router(supplier_router, prefix= '/supplier')
router.include_router(payment_router, prefix= '/payment')
router.include_router(productDiscount_router, prefix= '/productDiscount')
router.include_router(coupon_router, prefix= '/coupon')
router.include_router(customer_router, prefix= '/customer')
router.include_router(address_router, prefix= '/address')






