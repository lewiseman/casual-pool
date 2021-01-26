from django.urls import path, include
from .views import *

urlpatterns = [
    path('create_booking', createBooking, name='create_booking'),
    path('make_booking/<str:pk>', makeBooking, name='make_booking'),
    path('update_booking/<str:pk>', updateBooking, name='update_booking'),
    path('cancel_booking/<str:pk>', cancelBooking, name='cancel_booking'),
    path('accept_booking/<str:pk>', acceptBooking, name='accept_booking'),
    path('reject_booking/<str:pk>', rejectBooking, name='reject_booking'),
]