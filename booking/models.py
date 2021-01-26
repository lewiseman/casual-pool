from django.db import models
from manager.models import Manager
from educator.models import Educator

class Booking(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Cancelled', 'Cancelled'),
        )

    educator = models.ForeignKey(Educator, null=True, on_delete= models.SET_NULL)
    manager = models.ForeignKey(Manager, null=True, on_delete= models.SET_NULL)
    date = models.DateField(null=True)
    shift_start_time = models.TimeField(default='00:00', null=True)
    shift_end_time = models.TimeField(default='12:00', null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.educator.user.username

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
