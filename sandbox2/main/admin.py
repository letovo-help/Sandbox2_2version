from django.contrib import admin
from .models import Requests
from .models import Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Requests)