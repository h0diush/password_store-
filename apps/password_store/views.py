from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, UpdateView

from .decorators import password_required
from .forms import PasswordModelForm, PasswordStoreModelForm, \
    VerifyPasswordForm
from .mixins import DeleteViewMixin
from .models import PasswordsModel, PasswordStoreModel
from .utils import verify_password


def index(request):
    """Отображение главной страницы"""

    context = {
        'title': 'Главная'
    }
    return render(request, 'password_store/index.html', context)


def close_access_in_store(request):
    """Закрытие доступа к хранилищу паролей"""

    request.session['password_required_auth'] = False
    return redirect('/')


class CreatePasswordForAccessToPasswordStoreView(LoginRequiredMixin, FormView):
    """Создание пароля для доступа к хранилищу паролей"""

    form_class = PasswordModelForm
    template_name = 'password_store/create_password_access_to_store.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        password = PasswordsModel.objects.filter(
            user=self.request.user)
        context['there_is_password'] = password.exists()
        context['password'] = password.first()
        context['title'] = 'Пароль для доступа к хранилищу'
        return context

    def form_valid(self, form):
        if not PasswordsModel.objects.filter(user=self.request.user):
            form.instance.user = self.request.user
            form.save()
        return super().form_invalid(form)


class CreateMyPasswordView(LoginRequiredMixin, FormView):
    """Создание паролей в хранилище"""

    def dispatch(self, request, *args, **kwargs):
        if not PasswordsModel.objects.filter(
                user=request.user
        ).exists():
            return redirect(reverse('create_password_for_access_to_store'))
        return super().dispatch(request, *args, **kwargs)

    form_class = PasswordStoreModelForm
    template_name = 'password_store/create_password_in_store.html'
    success_url = reverse_lazy('my_password_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить пароль'
        return context


@login_required
def get_veryfi_password_view(
        request,
        template_name='password_store/password_veryfi.html',
        veryfi_password_form=VerifyPasswordForm
):
    """Функция проверки пароля для доступа к странице"""

    form = veryfi_password_form(data=request.POST)
    context = {
        'form': form,
        'title': 'Верификация доступа к хранилищу'
    }
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            try:
                model_password = PasswordsModel.objects.get(user=user)
                context.update({'password': model_password})
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


class ListPasswordView(LoginRequiredMixin, ListView):
    """Просмотр сохраненных паролей"""

    @password_required
    def dispatch(self, request, *args, **kwargs):
        if not PasswordsModel.objects.filter(
                user=request.user
        ).exists:
            return Http404
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'passwords'
    template_name = 'password_store/password_list_for_user.html'

    def get_queryset(self):
        return self.request.user.passwords_store.all

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои пароли'
        return context


class DeletePasswordInStoreView(DeleteViewMixin):
    """Удаление паролей в хранилище"""

    model = PasswordStoreModel

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class DeletePasswordInAccessStoreView(DeleteViewMixin):
    """Удаление пароля для доступа к хранилищу"""

    model = PasswordsModel
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class UpdatePasswordInAccessStoreView(UpdateView):
    """Обновление пароля для доступа к хранилищу"""

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            return Http404
        return super().dispatch(request, *args, **kwargs)

    model = PasswordsModel
    form_class = PasswordModelForm
    pk_url_kwarg = 'pk'
    template_name = 'password_store/update_access_for_password_store.html'
    context_object_name = 'password'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля для доступа к хранилищу'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
