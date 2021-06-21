from django.contrib import admin

# Register your models here.
from .models import Blog

admin.site.register(Blog)

admin.site.site_header = 'Bloggit Admin'
admin.site.site_title = 'Bloggit Admin Area'
admin.site.index_title = 'Welcome to the Bloggit admin area'