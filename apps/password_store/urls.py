from django.urls import path

from .views import (CreatePasswordForAccessToPasswordStoreView, index,
                    CreateMyPasswordView, get_veryfi_password_view,
                    ListPasswordView, DeletePasswordInStoreView,
                    close_access_in_store, DeletePasswordInAccessStoreView,
                    UpdatePasswordInAccessStoreView)

urlpatterns = [
    path('', index, name='index'),
    path('create_password_for_access_to_store/',
         CreatePasswordForAccessToPasswordStoreView.as_view(),
         name='create_password_for_access_to_store'),
    path('create_password_in_store/',
         CreateMyPasswordView.as_view(),
         name='create_password_in_store'),
    path('veryfi/', get_veryfi_password_view, name='verify'),
    path('my_passwords/', ListPasswordView.as_view(), name='my_password_list'),
    path('password/<int:pk>/delete/', DeletePasswordInStoreView.as_view(),
         name='delete_password_in_store'),
    path('password_aceess/<int:pk>/delete/',
         DeletePasswordInAccessStoreView.as_view(),
         name='delete_password_for_access_to_store'),
    path('password_aceess/<int:pk>/update/',
         UpdatePasswordInAccessStoreView.as_view(),
         name='update_password_for_access_to_store'),
    path('close_access/', close_access_in_store, name='close_access'),

]

"""
Суть приложения - это сохранение паролей для доступа к различным сайтам.
Доступа пользователя к личному хранилищу паролей осуществляется с 
предварительным вводом пароля
этот пароль можно создать, удалить и изменить
"""
