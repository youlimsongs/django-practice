from django.db import models
from asyncio import AbstractServer

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, AbstractUser
)

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) :
        return self.email
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.admin

