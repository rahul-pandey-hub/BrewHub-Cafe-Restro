# Generated by Django 4.1.3 on 2023-01-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0055_alter_cart_offer_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='offer_record',
            field=models.IntegerField(null=True),
        ),
    ]
