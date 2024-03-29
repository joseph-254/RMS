from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must provide a username")
        user_obj = self.model(email = self.normalize_email(email), username = username)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using = self._db)
        return user_obj
    
    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password= password,
            is_staff = True
        )
        return user

    def create_superuser(self, email,username, password=None):
        user = self.create_user(
            email,
            username,
            password= password,
            is_staff = True,
            is_admin = True
        )
        return user

class User(AbstractBaseUser):
    email   = models.EmailField(max_length = 255, unique= True)
    username = models.CharField(max_length =255)
    active  = models.BooleanField(default = True)
    staff   = models.BooleanField(default = False)
    admin   = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']

    objects = UserManager()  # Assign your custom manager to the objects attribute

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, odj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
