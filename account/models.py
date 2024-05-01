from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
#rom Booking.models import Profile




class Image(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='profile_pic' )

class User(AbstractUser):
    id              = models.CharField(primary_key=True,max_length=50, default=False)
    is_admin        = models.BooleanField(default=False)
    is_customer     = models.BooleanField(default=False)
    is_employee     = models.BooleanField(default=False)
    is_approved     = models.BooleanField(default=False, verbose_name='approved')  
    approve_login   = models.BooleanField(default=False, verbose_name='approve login')  # Add the new field
    email_confirmed = models.BooleanField(default=False)
    class Meta(AbstractUser.Meta):
        permissions = [
            ('can_add_group', 'Can add group'),
            ('can_delete_group', 'Can delete group'),
            ('can_change_group', 'Can change group'),
        ]
    def _str_(self):
        return self.id


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


def register_user(id, firstName, lastName, username, email, password, is_admin=False):
    user = User.objects.create_user( id=id, firstName=firstName, lastName=lastName, username=username, email=email, password=password)
  #  profile = Profile.object.create_Profile(user,img)
    request = RegistrationRequest.objects.create(user=user)
    if is_admin:
        user.is_staff = True
    else:
        user.is_active = False  # Deactivate user until approved
    user.save()
    
