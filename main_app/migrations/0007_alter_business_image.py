# Generated by Django 4.0.1 on 2022-02-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_business_photo_url_business_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(upload_to='businesscollector/'),
        ),
    ]
