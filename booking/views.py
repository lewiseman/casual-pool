from django.shortcuts import render, redirect
from availability.models import Availability
from .forms import BookingForm, JobBookingForm
from django.core.mail import send_mail
from .models import Booking

def createBooking(request):
    context = {}
    return render(request, 'create_booking.html', context)


def makeBooking(request, pk):
    try:
        availability = Availability.objects.get(id=pk)
    except Availability.DoesNotExist:
        return redirect('manager_home')
    manager = request.user.manager
    form = BookingForm(initial={'manager': manager, 'status':'Pending'}, instance=availability)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            send_mail(
            'Petit Casual Pool: You have a booking from <centre>',
            'accept_job.html',
            'from@example.com',
            [availability.educator.user.email],
            fail_silently=False,
            )
            print("hello")
            form.save()
            availability.delete()
            return redirect('manager_home')

    context = {'form':form}
    return render(request, 'make_booking.html', context)



def updateBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	form = BookingForm(instance=booking)

	if request.method == 'POST':
		form = BookingForm(request.POST, instance=booking)
		if form.is_valid():
			send_mail(
			'Petit Casual Pool: <centre> has updated a booking on <date>',
			'booking_email.html',
			'from@example.com',
			[booking.educator.user.email],
			fail_silently=False,
			)		
			form.save()
			return redirect('manager_home')

	context = {'form':form}
	return render(request, 'make_booking.html', context)



def cancelBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	if request.method == "POST":
		send_mail(
		'Petit Casual Pool: <centre> has cancelled a booking on <date>',
		'booking_email.html',
		'from@example.com',
		[booking.educator.user.email],
		fail_silently=False,
		)	
		booking.status = 'Cancelled'
		booking.save()
		return redirect('manager_home')

	context = {'item':booking}
	return render(request, 'cancel_booking.html', context)




def acceptBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	educator = request.user.educator
	form = JobBookingForm(initial={'educator':educator, 'status':'Accepted'}, instance=booking)

	if request.method == "POST":
		form = JobBookingForm(request.POST, instance=booking)
		if form.is_valid():
			send_mail(
			'Petit Casual Pool: <educator> has confirmed booking on <date>',
			'booking_email.html',
			'from@example.com',
			[booking.manager.user.email],
			fail_silently=False,
			)				
			form.save()
			booking.delete()
			return redirect('educator_home')

	context = {'item':booking, 'form':form}

	return render(request, 'accept_booking.html', context)	


def rejectBooking(request, pk):
	booking = Booking.objects.get(id=pk)
	if request.method == "POST":
		booking.status = 'Not Accepted'
		send_mail(
		'Petit Casual Pool: <educator> has declined a booking on <date>',
		'booking_email.html',
		'from@example.com',
		[booking.manager.user.email],
		fail_silently=False,
		)		
		booking.save()
		booking.delete()
		return redirect('educator_home')

	context = {'item':booking}

	return render(request, 'reject_booking.html', context)
