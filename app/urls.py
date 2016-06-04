from django.conf.urls import url, include

from . import views

#urls which send POST/GET data must not end with a slash

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
