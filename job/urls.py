from django.urls import path, include
from .views import *

urlpatterns = [
    path('accept_job/<str:pk>', acceptJob, name='accept_job'),
    path('create_job', createJob, name='create_job'),
    path('update_job/<str:pk>', updateJob, name='update_job'),
    path('delete_job/<str:pk>', deleteJob, name='delete_job'),
]