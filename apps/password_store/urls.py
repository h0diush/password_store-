from django.urls import path

from .views import (CreatePasswordForAccessToPasswordStoreView, index,
                    CreateMyPasswordView, get_veryfi_password_view,
                    ListPasswordView, DeletePasswordInStoreView,
                    close_access_in_store, DeletePasswordInAccessStoreView)

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
    path('close_access/', close_access_in_store, name='close_access'),

]
