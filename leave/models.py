from django.db import models
from educator.models import Educator



class Leaves(models.Model):
    LEAVETYPE = (
        ('Annual', 'Annual'),
        ('Sick', 'Sick'),
        ('Personal', 'Personal'),
        ('No pay', 'No pay'),
        ('Parental', 'Parental'),
        ('Other', 'Other'),
    )
    LEAVESTATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    educator = models.ForeignKey(Educator, null=True, on_delete= models.SET_NULL, blank=True)
    date_from = models.DateField(null=True)
    date_to = models.DateField( null=True)
    leave_type = models.CharField(max_length=200, null=True, choices=LEAVETYPE)
    leave_status = models.CharField(max_length=200, null=True, choices=LEAVESTATUS, default='Pending')
    description = models.TextField( null=True)

    def __str__(self):
        return self.leave_type

    class Meta:
        verbose_name = "Leave"
        verbose_name_plural = "Leaves"