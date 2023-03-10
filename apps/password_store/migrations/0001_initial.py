# Generated by Django 4.1.4 on 2023-01-04 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255, verbose_name='Пароль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пароль',
                'verbose_name_plural': 'Пароли',
            },
        ),
    ]
