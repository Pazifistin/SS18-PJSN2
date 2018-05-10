from django.urls import path, re_path
from . import views

app_name = 'todoBoard'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('new/new/', views.newsubmit, name='newSubmit'),
    re_path(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit'),
    re_path(r'^edit/(?P<pk>[0-9]+)/submit/$', views.editsubmit, name='editSubmit'),
    re_path(r'^edit/(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
]
