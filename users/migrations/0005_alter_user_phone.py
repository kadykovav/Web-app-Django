# Generated by Django 5.0.6 on 2024-06-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(null=True, unique=True, verbose_name='Телефон'),
        ),
    ]
