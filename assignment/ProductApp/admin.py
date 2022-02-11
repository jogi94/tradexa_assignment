from django.contrib import admin
from .models import *
# Register your models here.


#
@admin.register(product_model)
class product_modelAdmin(admin.ModelAdmin):
	list_display = ('name', 'weight', 'price',)
	list_filter = ('name', )