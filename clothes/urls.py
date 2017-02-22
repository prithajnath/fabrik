from django.conf.urls import url
from clothes import views

urlpatterns = [
    url(r'^$', views.index, name='closet'),
    url(r'^add/', views.add, name='add')
]
