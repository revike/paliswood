import hashlib
import random

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput

from auth_app.models import ShopUser


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'email': EmailInput(attrs={'required': 'required'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_email(self):
        email_user = self.cleaned_data['email']
        email_data = ShopUser.objects.filter(email=email_user)
        if email_data:
            raise forms.ValidationError(
                'Пользователь с таким email уже зарегистрирован'
            )
        return email_user

    def save(self, commit=True):
        user = super().save()
        user.is_active = True
        salt = hashlib.sha1(
            str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1(
            (user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user
