# Generated by Django 3.2.7 on 2022-09-29 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamburger', '0003_alter_mac_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.AlterField(
            model_name='burgerking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='mac',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='mos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='id'),
        ),
    ]
