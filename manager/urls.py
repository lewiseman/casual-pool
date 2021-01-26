from django.urls import path, include
from .views import *

urlpatterns = [
    path('', managerHome, name='manager_home'),
    path('educator_list', educatorList, name='educator_list'),
    path('delete_educator/<str:pk>', deleteEducator, name='delete_educator'),
]