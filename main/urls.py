from django.urls import path
from main import views as main_app

app_name = 'main'

urlpatterns = [
    path('', main_app.Index.as_view(), name='index'),
    path('catalog/', main_app.CatalogListView.as_view(), name='catalog'),
    path('category/<int:pk>', main_app.CategoryListView.as_view(),
         name='category'),
    path('buyers/', main_app.Buyers.as_view(), name='buyers'),
    path('about/', main_app.AboutMe.as_view(), name='about'),
]
