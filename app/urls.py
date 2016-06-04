from django.conf.urls import url, include
from . import views
# from .views import *
#urls which send POST/GET data must not end with a slash

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^Provider/$', views.index, name='index'),
    url(r'Provider/(?P<id>\w+)$', views.provider_info, name='provider_info'),
]
