# Generated by Django 3.0 on 2022-07-23 23:52

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220724_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[users.validators.UsernameValidator]),
        ),
    ]
