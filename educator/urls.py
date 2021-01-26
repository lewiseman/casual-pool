from django.urls import path, include
from .views import *

urlpatterns = [
    path('', educatorHome, name='educator_home'),
]