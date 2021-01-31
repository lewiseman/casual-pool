from django.urls import path
from . import views
from .models import Shift
from .views import ShiftWeekArchiveView

urlpatterns = [
    path('', views.rosterPage, name="roster"),
    path('<int:year>/week/<int:week>', ShiftWeekArchiveView.as_view(), name='archive_week')
]