from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from auth_app.forms import ShopUserRegisterForm
from main.models import Social, ProductCategory


class LoginUserView(LoginView):
    """Authentication"""
    template_name = 'auth_app/login.html'

    def get_context_data(self, **kwargs):
        next_url = self.request.META.get('HTTP_REFERER')
        self.request.session['next_url'] = next_url
        context = super().get_context_data(**kwargs)
        context['title'] = 'авторизация'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context

    def post(self, request, *args, **kwargs):
        super().post(self)
        try:
            if request.session['next_url'].split('/')[-2] == 'register':
                return HttpResponseRedirect(reverse('main:catalog'))
        except AttributeError:
            return HttpResponseRedirect(reverse('main:catalog'))
        return HttpResponseRedirect(request.session['next_url'])


class LogoutUserView(LogoutView):
    """Logout"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('auth_app:login'))


class RegisterUserView(generic.CreateView):
    """Register user"""
    template_name = 'auth_app/register.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'регистрация'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        username = register_form.data.get('username')
        password = register_form.data.get('password2')
        super().post(self)
        login_user = authenticate(username=username, password=password)
        login(request, login_user)
        return HttpResponseRedirect(reverse('main:catalog'))


class CabinetUserView(TemplateView):
    """Cabinet for user"""
    template_name = 'auth_app/cabinet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'личный кабинет'
        context['social'] = Social.get_social()
        context['categories'] = ProductCategory.get_category()
        return context
