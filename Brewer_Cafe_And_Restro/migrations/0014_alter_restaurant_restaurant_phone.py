# Generated by Django 4.1.3 on 2022-12-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0013_alter_user_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_phone',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
