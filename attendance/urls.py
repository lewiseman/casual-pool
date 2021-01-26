from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance, name="attendance"),
    path('human_resource', views.humanResource, name="human_resource"),
    path('pin_in/<str:pk>', views.pinSigninConfirmation, name="pin_in"),
    path('pin_out/<str:pk>', views.pinSignoutConfirmation, name="pin_out"),
    path('start_shift/<str:pk>', views.shiftStartInfo, name="start_shift"),
    path('end_shift/<str:pk>', views.shiftEndInfo, name="end_shift"),
]