from django.conf.urls import url
from clothes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add, name='add')
]
