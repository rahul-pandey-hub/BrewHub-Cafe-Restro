# Generated by Django 4.1.3 on 2022-12-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0010_alter_restaurant_restaurant_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_phone',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_mobile',
            field=models.DecimalField(decimal_places=0, max_digits=10, unique=True),
        ),
    ]
