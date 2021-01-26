from django.db import models
from educator.models import Educator

class Availability(models.Model):
    educator = models.ForeignKey(Educator, null=True, on_delete= models.SET_NULL)
    date = models.DateField(null=True)
    start_time = models.TimeField(default='06:30', null=True)
    end_time = models.TimeField(default='18:30', null=True)

    def __str__(self):
        return self.educator.user.username

    class Meta:
        verbose_name = "Availabile"
        verbose_name_plural = "Availability"
