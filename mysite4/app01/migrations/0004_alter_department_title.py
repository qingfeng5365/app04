# Generated by Django 4.1 on 2022-10-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='名称'),
        ),
    ]
