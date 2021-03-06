"""paliswood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from main.views import Error404

urlpatterns = [
    path('adminpaliswood/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('', include('auth_app.urls', namespace='auth_app')),
]

admin.site.site_header = "PalisWood Administrator"

handler404 = Error404.as_view()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   import debug_toolbar

   urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]

