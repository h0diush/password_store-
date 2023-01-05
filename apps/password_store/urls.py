from django.urls import path

from .views import (CreatePasswordForAccessToPasswordStoreView, index,
                    CreateMyPasswordView)

urlpatterns = [
    path('', index, name='index'),
    path('create_password_for_access_to_store/',
         CreatePasswordForAccessToPasswordStoreView.as_view(),
         name='create_password_for_access_to_store'),
    path('create_password_in_store/',
         CreateMyPasswordView.as_view(),
         name='create_password_in_store'),
]
