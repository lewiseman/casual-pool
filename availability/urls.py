from django.urls import path, include
from .views import *

urlpatterns = [
    path('add_availability', createAvailability, name='add_availability'),
    path('update_availability/<str:pk>', updateAvailability, name='update_availability'),
    path('delete_availability/<str:pk>', deleteAvailability, name='delete_availability'),
]