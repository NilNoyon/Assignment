from django.contrib import admin
from .models import Category,Game
from django.utils.html import format_html

admin.site.site_header = 'Assigement Task'

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','created','api_link')
	def api_link(self, obj):
	    api_link = 'http://localhost:8000/api/v1/category_list'
	    return format_html("<a href= %s >link</a>" % api_link)
	list_filter = ('name',)
	search_fields = (['name','created'])

class GameAdmin(admin.ModelAdmin):
	list_display = ('name','category','created','api_link')
	def api_link(self, obj):
	    api_link = 'http://localhost:8000/api/v1/game_list'
	    return format_html("<a href= %s >link</a>" % api_link)
	search_fields = (['name','category__name'])
	list_filter = ('name','category')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Game,GameAdmin)
# Register your models here.
