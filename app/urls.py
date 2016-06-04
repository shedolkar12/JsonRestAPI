from django.conf.urls import url, include
from . import views
# from .views import *
#urls which send POST/GET data must not end with a slash

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^Provider/$', views.index, name='index'),
    url(r'Provider/(?P<id>\w+)$', views.provider_info, name='provider_info'),
    url(r'Provider/(?P<id>\w+)/area/$', views.service_area, name='service_area'),
    # url(r'Provider/(?P<provider_id>\w+)/area/(?P<area_id>\w+)$', views.service_area, name='service_area'),
]
