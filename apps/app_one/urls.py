from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index), #do not put () next to index
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'(?P<my_val>\d+)$', views.show),
    url(r'(?P<my_val>\d+)/edit$', views.edit),
    url(r'(?P<my_val>\d+)/delete', views.destroy)
]