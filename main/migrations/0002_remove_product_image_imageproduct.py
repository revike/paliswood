# Generated by Django 4.0.1 on 2022-01-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='картинка')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='main.product', verbose_name='продукт')),
            ],
        ),
    ]
