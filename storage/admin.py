from django.contrib import admin
from .models import Storage, Category, Favorites

admin.site.register(Category)
admin.site.register(Favorites)
admin.site.register(Storage)
