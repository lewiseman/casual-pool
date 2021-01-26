from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    centre = models.CharField(max_length=200, null=True, default="melbourne")
    phone = models.IntegerField(null=True, default=0000)

    def __str__(self):
        return self.centre

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
