from fastapi import APIRouter
from .product.views import router as product_router
from .category.views import router as category_router
from .supplier.views import router as supplier_router
from .payment.views import router as payment_router
from .productDiscount.views import router as productDiscount_router
from .coupon.views import router as coupon_router
from .customer.views import router as customer_router
from .address.views import router as address_router
from .auth.views import router as auth_router







router = APIRouter()

router.include_router(product_router, prefix= '/products', tags = ['product'])
router.include_router(category_router, prefix= '/categories',  tags = ['category'])
router.include_router(supplier_router, prefix= '/suppliers',  tags = ['supplier'])
router.include_router(payment_router, prefix= '/payments',  tags = ['payment'])
router.include_router(productDiscount_router, prefix= '/productDiscounts',  tags = ['productDiscount'])
router.include_router(coupon_router, prefix= '/coupons',  tags = ['coupon'])
router.include_router(customer_router, prefix= '/customers',  tags = ['customer'])
router.include_router(address_router, prefix= '/address',  tags = ['address'])
router.include_router(auth_router, prefix= '/auth',  tags = ['auth'])







