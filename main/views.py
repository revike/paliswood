from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """Index"""
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'главная страница'
        return context


class Error404(TemplateView):
    """Error 404"""
    template_name = 'main/404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'error 404'
        return context
