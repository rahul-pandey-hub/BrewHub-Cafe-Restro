# Generated by Django 4.1.3 on 2022-12-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0009_alter_user_user_email_alter_user_user_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_phone',
            field=models.BigIntegerField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_mobile',
            field=models.BigIntegerField(max_length=10, unique=True),
        ),
    ]
