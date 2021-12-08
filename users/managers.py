from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class Roles(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

RESERVED_NAME = 'me'

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        """
        Сохраняет пользователя только с емаил, ником, паролем
        """
        if not email:
            raise ValueError('Поле email обязательное')
        if username == RESERVED_NAME:
            raise ValueError('Данное имя нельзя использовать')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault('is_active', True) 
        extra_fields.setdefault('role', Roles.ADMIN)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)