# Generated by Django 2.2 on 2020-01-08 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191226_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='parent_one',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent_one', to=settings.AUTH_USER_MODEL, verbose_name='Родитель Один'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='parent_two',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent_two', to=settings.AUTH_USER_MODEL, verbose_name='Родитель Два'),
        ),
    ]
