# Generated by Django 4.1.3 on 2022-12-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0022_alter_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
