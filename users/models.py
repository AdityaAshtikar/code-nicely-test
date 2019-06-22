from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
# from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phoneNumber, password=None, is_active=True, is_staff=False, is_admin=False):
        if not phoneNumber:
            raise ValueError("Users must have a phone number")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            phoneNumber=phoneNumber
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, phoneNumber, password=None):
        user = self.create_user(
            phoneNumber,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, phoneNumber, password=None):
        user = self.create_user(
            phoneNumber,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(
        max_length=50, blank=False, null=False, validators=[MinLengthValidator(3)])
    phoneNumber = models.CharField(max_length=10,
                                   validators=[RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)], unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phoneNumber'
    # REQUIRED_FIELDS = [full_name]

    objects = UserManager()

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
