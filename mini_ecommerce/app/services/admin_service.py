from fastapi import Depends


from app.repositories.admin_repository import AdminRepository

from app.api.admin.schemas import AdminSchema
from app.common.exceptions import AdminEmailAlreadyExistsException
from app.common.exceptions import AdminEmailNotExistsException




class AdminService:
    def __init__(self, admin_repository: AdminRepository = Depends()):
        self.admin_repository = admin_repository

    def create_admin(self, admin: AdminSchema):
        find_by_email = self.admin_repository.find_by_email(admin.email)
        if find_by_email:
                raise AdminEmailAlreadyExistsException()

        self.admin_repository.create(AdminSchema(**admin.dict()))

    def update_admin(self, admin: AdminSchema):
        find_by_email = self.admin_repository.find_by_email(admin.email)

        if find_by_email:
            self.admin_repository.update(AdminSchema(**admin.dict()))

        raise AdminEmailNotExistsException()