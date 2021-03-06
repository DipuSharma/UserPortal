# Generated by Django 3.2.6 on 2021-08-24 11:43

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
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sample_received', models.IntegerField()),
                ('Sequence_last', models.IntegerField()),
                ('Sample_pending', models.IntegerField(blank=True, null=True)),
                ('Sample_rejected', models.IntegerField(blank=True, null=True)),
                ('Reason', models.CharField(blank=True, max_length=200)),
                ('Remark', models.CharField(blank=True, max_length=200)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='username')),
            ],
        ),
    ]
