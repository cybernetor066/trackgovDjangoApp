# Generated by Django 3.1.1 on 2020-10-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trackgovApp', '0012_delete_userregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('firstname', models.CharField(db_column='FIRSTNAME', max_length=200)),
                ('lastname', models.CharField(db_column='LASTNAME', max_length=200)),
                ('useremail', models.EmailField(db_column='USEREMAIL', max_length=200, unique=True)),
                ('username', models.CharField(db_column='USERNAME', max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(db_column='PASSWORD', max_length=200)),
                ('datereg', models.DateTimeField()),
            ],
            options={
                'db_table': 'registered_users',
            },
        ),
    ]
