# Generated by Django 4.1.3 on 2022-12-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brewer_Cafe_And_Restro', '0018_alter_user_user_sec_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mobile',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]