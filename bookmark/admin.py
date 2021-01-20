from django.contrib import admin

# load Bookmark class(table) 
from .models import Bookmark


# Register your models here.
admin.site.register(Bookmark)