from django.conf.urls import url
from . import views


app_name = 'home'
urlpatterns = [
    # 127.0.0.1/Songs/
    url(r'^$', views.home, name='home'),
    url(r'^find$', views.find, name='find'),
    url(r'^sahil_kalra$', views.sahil, name='sahil'),
    ]
