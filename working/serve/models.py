from django.db import models
# Create your models here.
class data(models.Model):
	topic=models.CharField(max_length=20)
	level=models.CharField(max_length=10)
	question=models.CharField(max_length=100)
	answer=models.CharField(max_length=100)

	def __str__(self):
		return self.topic