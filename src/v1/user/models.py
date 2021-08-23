import datetime

from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class MyAccoutManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Пользователь должен иметь электронный адресс!")
        if not username:
            raise ValueError("Пользватель должен иметь логин!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    fio = models.CharField("Ваше Ф.И.О", max_length=150)
    email = models.EmailField("Электронный адрес")
    phone = models.CharField(max_length=14, blank=True, null=True)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=datetime.datetime.now())
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = MyAccoutManager()

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True
