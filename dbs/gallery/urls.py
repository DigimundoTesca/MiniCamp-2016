from django.conf.urls import url
from . import views

app_name = 'gallery'

urlpatterns = [
    url(r'^galeria/$', views.home, name='gallery'),
    url(r'^agregar/$', views.add_image, name='add'),
]
