from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^location/', views.location, name='location'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^setting/', views.setting, name='setting')
]
