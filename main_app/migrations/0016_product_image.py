# Generated by Django 4.0.1 on 2022-02-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', null=True, upload_to='businesscollector/'),
        ),
    ]
