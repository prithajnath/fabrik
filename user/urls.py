from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user import views

urlpatterns = [
    url(r'^location/', views.location, name='location')
]
