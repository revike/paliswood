from django.db import models


class ProductCategory(models.Model):
    """Model for Categories product"""

    class Meta:
        verbose_name_plural = 'категории'

    name = models.CharField(max_length=64, unique=True, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    is_active = models.BooleanField(default=True, verbose_name='активна',
                                    db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model for products"""

    class Meta:
        verbose_name_plural = 'продукты'

    category = models.ForeignKey(
        to=ProductCategory, on_delete=models.CASCADE, verbose_name='категория',
        db_index=True)
    name = models.CharField(max_length=128, verbose_name='название')
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    quantity = models.PositiveSmallIntegerField(
        default=0, verbose_name='количество на складе')
    is_active = models.BooleanField(default=True, verbose_name='активна',
                                    db_index=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category',
                                                               'name')


class ImageProduct(models.Model):
    """Model for Images"""
    product = models.ForeignKey(Product, related_name='images', default=None,
                                on_delete=models.CASCADE,
                                verbose_name='продукт')
    image = models.ImageField(
        upload_to='products_images', blank=True, verbose_name='картинка')
