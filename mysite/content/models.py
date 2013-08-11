from django.db import models

# Create your models here.
class post(models.Model):
	author = models.CharField(max_length = 50)
	title = models.CharField(max_length = 150)
	bodytext = models.TextField()
	timestamp = models.DateTimeField()
