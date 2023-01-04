from django.contrib.auth import get_user_model
from django.db import models

from .utils import hash_password

User = get_user_model()


class PasswordsModel(models.Model):
    """Модель пароля пользователя для доступа к хранилищу паролей"""

    user = models.ForeignKey(
        "users.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='passwords'
    )
    password = models.CharField(
        max_length=255,
        verbose_name='Пароль для доступа к хранилищу'
    )

    class Meta:
        verbose_name = 'Пароль для доступа к хранилищу'
        verbose_name_plural = 'Пароли для доступа к хранилищу'

    def __str__(self):
        return f'{self.password}'

    def save(self, *args, **kwargs):
        self.password = hash_password(self.password)
        return super().save(*args, **kwargs)


# TODO придумать как это лучше сделать либо CharField либо ManyToManyField
class PasswordStoreModel(models.Model):
    """ Модель хранилища паролей"""

    password = models.CharField(
        "Пароль", max_length=255,
    )
    user = models.ForeignKey(
        "users.User",
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='passwords_store'
    )

    class Meta:
        verbose_name = 'Пароль пользователя'
        verbose_name_plural = 'Пароли пользователя'

    def __str__(self):
        return f'Пароль №{self.pk}'