from django.urls import path
# from django.views.decorators.cache import cache_page
from main import views as main

app_name = 'main'

urlpatterns = [
    path('', main.Index.as_view(), name='index'),
]
