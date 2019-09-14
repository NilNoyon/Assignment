from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=100)
	image = models.FileField(upload_to='post_image', blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

