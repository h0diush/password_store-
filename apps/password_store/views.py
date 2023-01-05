from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView

from .decorators import password_required
from .forms import PasswordModelForm, PasswordStoreModelForm, \
    VerifyPasswordForm
from .models import PasswordsModel
from .utils import verify_password


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


@login_required
def get_veryfi_password_view(
        request,
        template_name='password_store/password_veryfi.html',
        veryfi_password_form=VerifyPasswordForm
):
    """Функция проверки пароля для доступа к странице"""

    form = veryfi_password_form(data=request.POST)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            try:
                model_password = PasswordsModel.objects.get(user=user)
            except ObjectDoesNotExist:
                return redirect(reverse('create_password_for_access_to_store'))
            password = form.cleaned_data['password']
            if verify_password(password, model_password.password):
                request.session['password_required_auth'] = True
                return redirect(reverse('my_password_list'))
            context.update({'message': 'Пароль не правильный'})

            return render(request, template_name, context=context)
    else:
        return render(request, template_name, context=context)


# @password_required
class ListPasswordView(LoginRequiredMixin, ListView):
    """Просмотр сохраненных паролей"""

    @password_required
    def dispatch(self, request, *args, **kwargs):
        # request.session['password_required_auth'] = False
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'passwords'
    template_name = 'password_store/password_list_for_user.html'

    def get_queryset(self):
        return self.request.user.passwords_store.all
