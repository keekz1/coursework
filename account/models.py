from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False, verbose_name='approved')  
    approve_login = models.BooleanField(default=False, verbose_name='approve login')  # Add the new field
    email_confirmed = models.BooleanField(default=False)

    custom_groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_users') 
    custom_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_users')

    class Meta(AbstractUser.Meta):
        permissions = [
            ('can_add_group', 'Can add group'),
            ('can_delete_group', 'Can delete group'),
            ('can_change_group', 'Can change group'),
        ]


class RegistrationRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration_request')
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()
        user_instance = self.user
        user_instance.is_active = True
        user_instance.is_approved = True
        user_instance.save()


def register_user(username, email, password, is_admin=False):
    user = User.objects.create_user(username=username, email=email, password=password)
    request = RegistrationRequest.objects.create(user=user)
    if is_admin:
        user.is_staff = True
    else:
        user.is_active = False  # Deactivate user until approved
    user.save()
    
