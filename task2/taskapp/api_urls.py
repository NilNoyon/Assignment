from rest_framework import routers
from django.urls import path,include
from . import api_views
from django.urls import path
from taskapp.api_views import *
router = routers.DefaultRouter()


urlpatterns = [
	path('',include(router.urls)),
	path('category_list', api_views.CategoryAPI.as_view(),name='category_list'),
	path('game_list', api_views.GameAPI.as_view(),name='game_list'),
]