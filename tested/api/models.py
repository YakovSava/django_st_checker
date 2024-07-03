from django.db import models

class Company(models.Model):
	fcs = models.TextField(blank=False)
	date = models.TextField(blank=False) # strftime
	company_name = models.CharField(max_length=255)
	fcs_commissions1 = models.TextField(blank=False)
	commisions_status1 = models.TextField(blank=False)
	fcs_commissions2 = models.TextField(blank=False)
	commisions_status2 = models.TextField(blank=False)
	fcs_commissions3 = models.TextField(blank=False)
	commisions_status3 = models.TextField(blank=False)
	responsible_electrical_safety = models.TextField(blank=False)
	reason_for_check = models.TextField(blank=False)
	antifire_reason = models.TextField(blank=False)
	status = models.CharField(max_length=50)
	number_of_driver_program = models.CharField(max_length=1)
	electrical_safety_group = models.CharField(max_length=3)
	work_exp = models.CharField(max_length=2)
	session = models.TextField(blank=False)