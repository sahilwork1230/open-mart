from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        identifier = username
        if not identifier or not password:
            return None
        users = User.objects.filter(
            Q(username = identifier) | Q(email = identifier)
        )

        user = users.first()
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None
