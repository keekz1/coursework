from django.contrib.auth.backends import ModelBackend

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username=username, password=password, **kwargs)
        if user and hasattr(user, 'is_approved') and not user.is_approved:
            return None
        return user
