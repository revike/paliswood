# Generated by Django 4.0.1 on 2022-01-06 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('description', models.TextField(verbose_name='описание')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='активна')),
            ],
            options={
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='картинка')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='количество на складе')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='активна')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name_plural': 'продукты',
            },
        ),
    ]