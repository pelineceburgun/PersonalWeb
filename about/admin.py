from django.contrib import admin

# Register your models here.
from .models import Post,Page
admin.site.register(Post)
admin.site.register(Page)
