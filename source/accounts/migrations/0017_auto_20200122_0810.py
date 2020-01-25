# Generated by Django 2.2 on 2020-01-22 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_merge_20200122_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport',
            name='citizenship',
            field=models.CharField(default='Кыргызская Республика', max_length=20, verbose_name='Гражданство'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='inn',
            field=models.CharField(blank='True', max_length=50, null='True', verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='issued_by',
            field=models.CharField(blank='True', max_length=255, null='True', verbose_name='Кем выдан'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='nationality',
            field=models.CharField(blank='True', max_length=30, null='True', verbose_name='Национальность'),
        ),
    ]
