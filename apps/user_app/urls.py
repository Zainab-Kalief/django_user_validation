from django.conf.urls import url
from . import views
app_name='users'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up$', views.dataTest, name='sign_up'),
    url(r'^log_in$', views.loginTest, name='log_in'),
    url(r'^result/(?P<id>\d+)$', views.result, name=''),
]
