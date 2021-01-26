from django.shortcuts import render, redirect
from educator.models import Educator
from datetime import date, datetime, timedelta
from availability.models import Availability
from booking.models import Booking
from job.models import Job

def managerHome(request):
    startdate = date.today()
    enddate = startdate + timedelta(days=30)
    availability = Availability.objects.filter(date__range=[startdate, enddate]).order_by('date')
    booking_start_today = Booking.objects.filter(date__range=[startdate, enddate]).order_by('date')
    job_start_today = Job.objects.filter(date__range=[startdate, enddate]).order_by('date')

    context = {'availability':availability, 'booking':booking_start_today, 'jobs':job_start_today}
    return render(request, 'manager.html', context)

def educatorList(request):
    educators = Educator.objects.all()
    context = {'educators':educators}
    return render(request, 'educator_list.html', context)


def deleteEducator(request, pk):
	educator = Educator.objects.get(id=pk)
	if request.method == "POST":
		educator.user.delete()
		return redirect('/staffing')

	context = {'item':educator}
	return render(request, 'delete_educator.html', context)