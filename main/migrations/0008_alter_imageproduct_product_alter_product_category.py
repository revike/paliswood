# Generated by Django 4.0.1 on 2022-01-09 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_social_options_alter_social_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproduct',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.product', verbose_name='продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategory', verbose_name='категория'),
        ),
    ]
