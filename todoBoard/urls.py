from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.edit, name='edit'),
]
