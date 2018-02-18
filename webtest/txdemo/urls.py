from django.conf.urls import url
from txdemo import views


urlpatterns = (
    url('^$', views.index),
    url('^(\d+)/$', views.detail),
    url('^signup/$', views.signup),
)
