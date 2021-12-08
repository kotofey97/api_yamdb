from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
from .managers import Roles

class User(AbstractUser):
    
    username = models.CharField(
        verbose_name='Никнейм',
        blank=False, 
        unique=True,
        max_length=30,
    )
    email = models.EmailField(
        verbose_name='Почта',
        blank=False, 
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        blank=True,
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        max_length=50,
    )
    bio = models.TextField(
        verbose_name='О себе',
        blank=True,
        max_length=500,
    )
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=30,
        default=Roles.USER,
        choices=Roles.choices,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == Roles.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR or self.is_superuser

    class Meta(AbstractUser.Meta): 
        ordering = ['username'] 
        verbose_name = 'Пользователь' 
        verbose_name_plural = 'Пользователи' 
 
    def __str__(self): 
        return self.username 