from django.db import models
from educator.models import Educator

class Attendance(models.Model):
	shift_item = models.ForeignKey(Educator, null=True, on_delete=models.SET_NULL,  blank=True) 
	start_time = models.TimeField(null=True)
	end_time = models.TimeField(null=True)
