# Generated by Django 2.2.14 on 2020-07-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_order_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
