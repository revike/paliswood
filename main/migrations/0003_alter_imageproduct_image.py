# Generated by Django 4.0.1 on 2022-01-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_product_image_imageproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images/<django.db.models.query_utils.DeferredAttribute object at 0x0000028B3840EB80>', verbose_name='картинка'),
        ),
    ]
