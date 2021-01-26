from django.db import models
from django.contrib.auth.models import User

class Educator(models.Model):
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

    ROOMS = (
            ('Baby Room 0 - 12', 'Baby Room 0 - 12'),
            ('Toddlers Room 12 - 18', 'Toddlers Room 12 - 18'),
            ('Support Staff', 'Support Staff'),
            )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mobile = models.IntegerField(null=True, default=0000)
    qualification = models.CharField(max_length=200, null=True, choices=QUALIFICATION)
    profile_pic = models.ImageField(upload_to="profiles", default="profile.png", null=True, blank=True)
    room = models.CharField(max_length=200, null=True, choices=ROOMS, blank=True)
    pin = models.CharField(max_length=4, null=True, default="1234")
    date_created = models.DateField(auto_now_add=True, null=True)
        
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Educator"
        verbose_name_plural = "Educators"
