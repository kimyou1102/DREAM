# Generated by Django 3.2.5 on 2021-07-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomBaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=125, verbose_name='password')),
            ],
        ),
    ]
