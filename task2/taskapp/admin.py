from django.contrib import admin
from .models import Category,Game

admin.site.site_header = 'Assigement Task'

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','created')
	list_filter = ('name',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('name','category','created')
	list_filter = ('name','category')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Game,GameAdmin)
# Register your models here.
