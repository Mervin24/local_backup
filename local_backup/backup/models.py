from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200)
	password = models.CharField(max_length=500)

class File(models.Model):
	url = models.CharField(max_length=1000)
	name = models.CharField(max_length=200)
	extension = models.CharField(max_length=200)
	uploaded_by = models.CharField(max_length=200)
	uploaded_on = models.DateField()
	size = models.IntegerField(default=0)

