# Generated by Django 4.1.3 on 2023-02-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0072_order_is_cancel_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablereservation',
            name='is_table_reservation_cancel',
            field=models.IntegerField(null=True),
        ),
    ]