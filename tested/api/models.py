from django.db import models

class Users(models.Model):
	name = models.CharField(max_length=255)
	is_admin = models.BooleanField(default=False)