from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
  path('', views.index, name='index'),
  path('read/<int:blog_id>', views.singleBlog, name='singleBlog')
]