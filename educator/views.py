from django.shortcuts import render
from datetime import date, datetime, timedelta
from .models import Educator
from job.models import Job

def educatorHome(request):
    startdate = date.today()
    enddate = startdate + timedelta(days=30)
    educator = Educator.objects.all()
    availability_start_today = request.user.educator.availability_set.all().filter(date__range=[startdate, enddate]).order_by('date')
    booking_start_today = request.user.educator.booking_set.all().filter(date__range=[startdate, enddate]).order_by('date')
    job_start_today = Job.objects.all().filter(date__range=[startdate, enddate]).order_by('date')
    
    context = {'jobs':job_start_today, 'bookings':booking_start_today, 'availability':availability_start_today}
    return render(request, 'educator.html', context)
