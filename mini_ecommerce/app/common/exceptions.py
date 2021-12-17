class PaymentMethodsNotAvailableException(Exception):
    def __init__(self):
        self.message = 'This payment method is not available'
        super().__init__(self.message)


class PaymentMethodDiscountAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'Already exists a discount with this payment method'
        super().__init__(self.message)


class CouponCodeAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'This code is already been used'
        super().__init__(self.message)

class CouponCodeNotExistsException(Exception):
    def __init__(self):
        self.message = 'This code not exists, please create this'
class ProductDiscountIdAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'This id is already been used'

class AdminEmailAlreadyExistsException(Exception):
    def __init__(self):
        self.message = 'This email is already been used'

class AdminEmailNotExistsException(Exception):
    def __init__(self):
        self.message = 'This email not exists, make create this'

class ProductDiscountIdNotExistsException(Exception):
    def __init__(self):
        self.message = 'This id not exists, make create this'