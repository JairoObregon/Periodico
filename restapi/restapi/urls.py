"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from models.views import postView,categoryView,postcategoryView, postcategoryView, imagenesView,portadaView,politicaView,policialView,deportesView,entretenimientoView,viajesView
from django.conf import settings 

router = routers.DefaultRouter()
router.register('post', postView, basename='post')
router.register('category', categoryView, basename='category')
router.register('imagen', imagenesView, basename='imagen')
router.register('portada', portadaView, basename='portada')
router.register('politica', politicaView, basename='politica')
router.register('policial', policialView, basename='policial')
router.register('deportes', deportesView, basename='deportes')
router.register('entretenimiento', entretenimientoView, basename='entretenimiento')
router.register('viajes', viajesView, basename='viajes')
router.register('posts/(?P<username>.+)', postcategoryView, basename='MyModel')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,include(router.urls)),
]

if settings.DEBUG :
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)