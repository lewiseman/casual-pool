from django.urls import path, include
from .views import *

urlpatterns = [
    path('leave', leave, name='leave'),
    path('new_leave', newLeave, name='new_leave'),
    path('update_leave_educator/<str:pk>', UpdateLeaveEducator, name='update_leave_educator'),
    path('update_leave_manager/<str:pk>', UpdateLeaveManager, name='update_leave_manager'),
]