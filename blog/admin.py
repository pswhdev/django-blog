from django.contrib import admin
from .models import Post, Comment

# Register your models here.

#So that the custom model created appears in the admin site
admin.site.register(Post)
admin.site.register(Comment)