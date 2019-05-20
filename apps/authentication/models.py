from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import admin

from apps.utils import TimeStampedModel

class UserManager(BaseUserManager):
    def create_user(self, username, student_id, password=None):
        if not username:
            raise ValueError('유저네임을 내놔라')
        
        if not student_id:
            raise ValueError('학번을 내놔라')

        user = self.model(username=username, student_id=student_id)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, student_id, password=None):
            superuser = self.create_user(username, student_id, password)
            superuser.is_superuser = True
            superuser.is_staff = True
            superuser.save()
            return superuser


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    username = models.CharField(max_length=64, unique=True, db_index=True)
    student_id = models.CharField(max_length=32)
    
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['student_id']

    objects = UserManager()

admin.site.register(User)