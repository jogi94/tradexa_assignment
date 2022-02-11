from django.contrib import admin
from .models import *
# Register your models here.


#
@admin.register(post_model)
class post_modelAdmin(admin.ModelAdmin):
	list_display = ( 'text','user',)
	list_filter = ('user', )