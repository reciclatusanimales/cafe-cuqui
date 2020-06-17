from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Meal, Category

class MealAdmin(SummernoteModelAdmin):
    summernote_fields = ['description']
    list_display = ['name', 'preparation_time', 'people', 'price']
    list_filter = ['category', 'people']
    search_fields = ['name', 'description']

admin.site.register(Meal, MealAdmin)
admin.site.register(Category)
