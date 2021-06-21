from django.shortcuts import render

from .models import Blog

# Create your views here.
def index(request):
  blog_list = Blog.objects.order_by('-pub_date')
  return render(request, 'blogs/index.html', {'blog_list': blog_list})