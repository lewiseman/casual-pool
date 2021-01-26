from django.db import models
from manager.models import Manager

class Job(models.Model):
    QUALIFICATION = (
            ('Working Towards Cert III', 'Working Towards Cert III'),
            ('Cert III', 'Cert III'),
            ('Working Towards Diploma', 'Working Towards Diploma'),
            ('Diploma', 'Diploma'),
            ('Working Towards Degree', 'Working Towards Degree'),
            ('Degree', 'Degree'),
            ('Working Towards Master Degree', 'Working Towards Master Degree'),
            ('Master Degree', 'Master Degree'),
            ('Others', 'Others'),
            )

    manager = models.ForeignKey(Manager, null=True, on_delete= models.SET_NULL)
    date = models.DateField(null=True)
    shift_start_time = models.TimeField(default='00:00', null=True)
    shift_end_time = models.TimeField(default='12:00', null=True)
    qualification = models.CharField(default='Cert III or above', max_length=200, null=True, choices=QUALIFICATION)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.manager.user.username

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"
