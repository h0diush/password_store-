from django import forms

from .models import PasswordsModel, PasswordStoreModel


class PasswordModelForm(forms.ModelForm):
    """Форма для создания доступа к хранилищу паролей"""

    password = forms.CharField(
        label='Пароль для доступа к хранилищу',
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = PasswordsModel
        fields = ('password',)


class PasswordStoreModelForm(forms.ModelForm):
    """Форма создания паролей в хранилище паролей"""

    description = forms.CharField(label='Описание', required=False,
                                  help_text='Не обязательно',
                                  widget=forms.Textarea()
                                  )
    username = forms.CharField(label='Имя пользователя',
                               help_text='Не обязательно', required=False,
                               widget=forms.TextInput())
    email = forms.EmailField(label='Электронная почта',
                             help_text='Не обязательно', required=False,
                             widget=forms.EmailInput())
    password = forms.CharField(label='Пароль', widget=forms.TextInput())

    class Meta:
        model = PasswordStoreModel
        exclude = ('user',)
