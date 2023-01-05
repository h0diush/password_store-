from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView

from .forms import PasswordModelForm, PasswordStoreModelForm
from .models import PasswordsModel


def index(request):
    return render(request, 'password_store/index.html')


class CreatePasswordForAccessToPasswordStoreView(LoginRequiredMixin, FormView):
    """Создание пароля для доступа к хранилищу паролей"""

    form_class = PasswordModelForm
    template_name = 'password_store/create_password_access_to_store.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password'] = PasswordsModel.objects.filter(
            user=self.request.user).exists()
        return context

    def form_valid(self, form):
        if not PasswordsModel.objects.filter(user=self.request.user):
            form.instance.user = self.request.user
            form.save()
        return super().form_invalid(form)


class CreateMyPasswordView(LoginRequiredMixin, FormView):
    """Создание паролей в хранилище"""

    form_class = PasswordStoreModelForm
    template_name = 'password_store/create_password_in_store.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
