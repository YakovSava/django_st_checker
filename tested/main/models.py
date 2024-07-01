from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=255)
	session = models.TextField(blank=False)
	company = models.TextField(blank=False)
	is_admin = models.BooleanField(default=False)
	login = models.TextField(blank=False)
	password = models.TextField(blank=False)