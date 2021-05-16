from django.urls import path,include

from . import views
app_name='gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('gallery', views.gallery, name='gallery'),
]
