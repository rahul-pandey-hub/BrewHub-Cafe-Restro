# Generated by Django 4.1.3 on 2023-01-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0034_alter_user_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forgot_password_token',
            field=models.CharField(default='', max_length=100),
        ),
    ]