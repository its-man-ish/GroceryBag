# Generated by Django 3.2.5 on 2021-07-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_mylist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylist',
            name='date',
        ),
        migrations.AlterField(
            model_name='mylist',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
