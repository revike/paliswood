from django.urls import path
from main import views as main

app_name = 'main'

urlpatterns = [
    path('', main.Index.as_view(), name='index'),
    path('catalog/', main.CatalogListView.as_view(), name='catalog'),
    path('category/<int:pk>', main.CategoryListView.as_view(),
         name='category'),
    path('buyers/', main.Buyers.as_view(), name='buyers'),
    path('about/', main.AboutMe.as_view(), name='about'),
]
