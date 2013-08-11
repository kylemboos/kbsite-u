from django.db import models

# Create your models here.
class posts(models.Model):
	author = models.CharField(max_length = 50)
	title = models.CharField(max_length = 150)
	bodytext = models.TextField()
	timestamp = models.DateTimeField()
