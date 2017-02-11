from django.conf.urls import url
from clothes import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
