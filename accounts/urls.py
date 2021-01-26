from django.urls import path, include
from .views import *

urlpatterns = [
    path('', profile, name='profile'),
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
    path('update_educator/<str:pk>', updateEducator, name='update_educator'),
]