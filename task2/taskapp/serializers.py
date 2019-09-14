from rest_framework import serializers
from rest_framework_bulk.drf3.serializers import BulkSerializerMixin, BulkListSerializer
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from taskapp.models import Category,Game

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = '__all__'

class GameListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Game
		fields = '__all__'
