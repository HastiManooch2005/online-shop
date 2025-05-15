from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import MyUser

class EmailBackend(BaseBackend):
    def authenticate(self, email,password):
        try:
            user = MyUser.objects.get(email=email)
            if user.check_password(password) :
                return user
            else: return None
        except MyUser.DoesNotExist:
            return None


    def get_user(self,user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None