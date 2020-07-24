from django.db import models

# Create your models here.

class Blog(models.Model):
	blogTitle = models.CharField(max_length=100)
	