# Generated by Django 3.1.1 on 2020-10-13 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackgovApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='date_pub',
            new_name='datereg',
        ),
    ]
