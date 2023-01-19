from functools import wraps

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import PasswordsModel


def password_required(view_func=None):
    """Декоратор запроса пароля для доступа к странице """

    def _wrapped_view(self, request, *args, **kwargs):
        password = PasswordsModel.objects.filter(user=request.user).exists()
        if not password:
            return HttpResponseRedirect(
                reverse('create_password_for_access_to_store'))
        if request.session.get('password_required_auth', False):
            return view_func(self, request, *args, **kwargs)
        return HttpResponseRedirect(reverse('verify'))

    return wraps(view_func)(_wrapped_view)
