from django.db import models

class Company(models.Model):
	company_name = models.CharField(max_length=255)
	company_admin = models.TextField(blank=False) # session
	is_super_admin = models.BooleanField(default=False)