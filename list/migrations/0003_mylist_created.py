# Generated by Django 3.2.5 on 2021-07-07 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_rename_user_mylist_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]