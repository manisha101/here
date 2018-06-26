from django.db import models
# Create your models here.
class data(models.Model):
	Topic=models.CharField(max_length=20)
	Level=models.CharField(max_length=10)
	Question=models.CharField(max_length=100)
	Answer=models.CharField(max_length=100)

	def __str__(self):
		return self.Topic