# Generated by Django 4.0.1 on 2022-01-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_imageproduct_product_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
    ]