# Generated by Django 4.1.3 on 2023-01-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0033_rename_title_itemcategory_item_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=300),
        ),
    ]
