# Generated by Django 4.1 on 2022-11-16 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_alter_task_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=64, verbose_name='头像')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='管理员')),
            ],
        ),
    ]
