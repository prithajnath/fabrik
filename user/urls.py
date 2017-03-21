from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user import views

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name' : 'user/login.html'}),
    url(r'^logout/', auth_views.logout, {'template_name' : 'user/logout.html'}),
    url(r'^register/', views.register, name='register'),
    url(r'^location/', views.location, name='location')
]
