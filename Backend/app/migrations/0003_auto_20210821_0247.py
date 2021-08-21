# Generated by Django 2.2.13 on 2021-08-20 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210821_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='username'),
        ),
    ]
