from django import forms
from .models import PasswordsModel


class PasswordModelForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль для доступа к хранилищу',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = PasswordsModel
        fields = ('password',)
