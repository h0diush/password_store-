from django.contrib import admin

from .models import PasswordsModel, PasswordStoreModel


@admin.register(PasswordsModel)
class PasswordModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'password')
    search_fields = ('user',)
    list_filter = ('user',)
    list_display_links = ('user',)


@admin.register(PasswordStoreModel)
class PasswordStoreModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'password')
    search_fields = ('user',)
    list_filter = ('user',)
    list_display_links = ('user',)
