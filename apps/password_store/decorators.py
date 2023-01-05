from functools import wraps

from django.http import HttpResponseRedirect
from django.urls import reverse


def password_required(view_func=None):
    """Декоратор запроса пароля для доступа к странице """

    def _wrapped_view(self, request, *args, **kwargs):
        if request.session.get('password_required_auth', False):
            return view_func(self, request, *args, **kwargs)
        return HttpResponseRedirect(reverse('verify'))

    return wraps(view_func)(_wrapped_view)
