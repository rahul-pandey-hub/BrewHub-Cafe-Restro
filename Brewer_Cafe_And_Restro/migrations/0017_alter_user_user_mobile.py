# Generated by Django 4.1.3 on 2022-12-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0016_alter_user_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mobile',
            field=models.DecimalField(decimal_places=0, max_digits=10, unique=True),
        ),
    ]
