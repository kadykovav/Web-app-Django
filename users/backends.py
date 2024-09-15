from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(username)
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=user_id)
            return user
        except UserModel.DoesNotExist:
            return None
