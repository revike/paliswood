from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class ShopUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользователи'

    avatar = models.ImageField(
        upload_to='users_avatars', blank=True, verbose_name='аватар')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

    def __str__(self):
        return f'{self.username} {self.first_name.title()} ' \
               f'{self.last_name.title()}'


class ShopUserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'профиль пользователя'
        verbose_name = 'профиль пользователя'

    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(
        ShopUser, unique=True, null=False, db_index=True,
        on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True,
                                  verbose_name='дата рождения')
    about_me = models.TextField(blank=True, verbose_name='о себе')
    gender = models.CharField(max_length=1, blank=True,
                              choices=GENDER_CHOICES, verbose_name='пол')

    # @receiver(post_save, sender=ShopUser)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         ShopUserProfile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=ShopUser)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.shopuserprofile.save()
