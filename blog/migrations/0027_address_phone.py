# Generated by Django 2.2.14 on 2020-07-22 06:44

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
