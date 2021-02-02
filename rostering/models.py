from django.db import models
from educator.models import Educator

class Shift(models.Model):
    STIME = (
        ('1 hr', '1 hr'),
        ('30 min', '30 min'),
        ('1 hr 30min', '1 hr 30min'),
        ('2 hr', '2 hr'),
    )
    educator_shift = models.ForeignKey(Educator, null=True, on_delete=models.SET_NULL, blank=True)
    date = models.DateField(null=True)
    shift_start = models.TimeField(blank=True, null=True)
    shift_end = models.TimeField(blank=True, null=True)
    lunch = models.CharField(max_length=200, null=True, choices=STIME)

    def __str__(self):
        return self.educator_shift.user.username

    def day_date(self):
        dy = str(self.date)
        day = dy[-2:]
        return int(day)

class Holidays(models.Model):
    name = models.CharField(max_length=200, null= True, blank=True)
    date = models.DateField(null=True)
    description = models.TextField(null=True)