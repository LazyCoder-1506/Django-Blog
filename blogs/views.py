from django.shortcuts import render

from .models import Blog

# Create your views here.
def index(request):
  blog_list = Blog.objects.order_by('-pub_date')
  return render(request, 'blogs/index.html', {'blog_list': blog_list})

def singleBlog(request, blog_id):
  blog_item = Blog.objects.get(pk=blog_id)
  return render(request, 'blogs/single_blog.html', {'blog_item': blog_item})