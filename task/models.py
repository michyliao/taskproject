from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.title

  	class Meta:
  		ordering = ['date_created']

