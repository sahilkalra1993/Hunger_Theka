from django.conf.urls import url
from . import views


app_name = 'menu'
urlpatterns = [
    # 127.0.0.1/Songs/
    url(r'^$', views.menu, name='menu'),
    url(r'^(?P<menu_id>[0-9]+)/detail/$', views.detail, name='detail'),
    ]
