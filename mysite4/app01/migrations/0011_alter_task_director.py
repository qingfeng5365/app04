# Generated by Django 4.1 on 2022-11-16 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_alter_task_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='负责人'),
        ),
    ]
