from django.contrib import admin
from .models import DishCategory, Dish
# Register your models here.

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

@admin.register(Dish)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
