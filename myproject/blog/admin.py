from django.contrib import admin
from .models import blog_post


@admin.register(blog_post)
class blog_postModel(admin.ModelAdmin):
    list_display = ['id','title','desc']

