from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self,username, password=None, email=None):
        if not username:
            raise ValueError("Users must have phone or email")

        user = self.model(
           username=username,
            email=self.normalize_email(email) if email else None,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password=None, email=None):
        user = self.create_user(
           username=username,
            password=password,
            email=email
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
