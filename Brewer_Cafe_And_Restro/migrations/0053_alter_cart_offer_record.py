# Generated by Django 4.1.3 on 2023-01-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0052_alter_cart_offer_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='offer_record',
            field=models.IntegerField(default=1),
        ),
    ]
