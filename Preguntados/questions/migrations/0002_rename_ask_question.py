# Generated by Django 3.2.8 on 2021-12-02 01:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ask',
            new_name='Question',
        ),
    ]
