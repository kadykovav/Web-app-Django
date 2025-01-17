# Generated by Django 5.0.6 on 2024-06-12 12:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, null=True, verbose_name='Роль пользователя')),
            ],
            options={
                'verbose_name': 'Роль пользователей',
                'verbose_name_plural': 'Роль пользователей',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.roleuser'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ManyToManyField(limit_choices_to={'role__title': 'Ученик'}, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(limit_choices_to={'role__title': 'Учитель'}, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Учителя и их ученики',
                'verbose_name_plural': 'Учителя и их ученики',
            },
        ),
    ]
