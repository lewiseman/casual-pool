from django.shortcuts import render, redirect
from .forms import StartShiftForm, EndShiftForm
from rostering.models import Shift
from datetime import date
from django.contrib import messages
from educator.models import Educator


def attendance(request):
    today = date.today()
    shifts = Shift.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
    #rooms = Room.objects.all()
    staffs = Educator.objects.all()
    context = {'shifts':shifts, 'staffs':staffs, 'today':today,}
    return render(request, 'attendance.html', context)


def pinSigninConfirmation(request, pk):
    educator_valid = Shift.objects.get(id=pk)
    educator_pin = educator_valid.educator_shift.pin
    context ={'staff_valid':educator_valid, 'staff_pin':educator_pin}
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if educator_pin == pin:
            return redirect('/attendance/start_shift/' + pk)
        else:
            messages.warning(request, 'Wrong pin entered')
            return redirect('/attendance/pin_in/' + pk)
    return render(request, 'pin.html', context)



def pinSignoutConfirmation(request, pk):
    educator_valid = Shift.objects.get(id=pk)
    educator_pin = educator_valid.educator_shift.pin
    context ={'staff_valid':educator_valid, 'staff_pin':educator_pin}
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if educator_pin == pin:
            return redirect('/attendance/end_shift/' + pk)
        else:
            messages.warning(request, 'Wrong pin entered')
            return redirect('/attendance/pin_out/' + pk)
    return render(request, 'pin.html', context)


def shiftStartInfo(request, pk):
    shift_info = Shift.objects.get(id=pk)
    form = StartShiftForm(instance=shift_info)
    if request.method == 'POST':
	    form = StartShiftForm(request.POST, instance=shift_info)

	    if form.is_valid():
                form.save()
                return redirect('attendance')

    context = {'shift_info':shift_info, 'form':form}
    return render(request, 'start_info.html', context)


def shiftEndInfo(request, pk):
    shift_info = Shift.objects.get(id=pk)
    form = EndShiftForm(instance=shift_info)
    if request.method == 'POST':
	    form = EndShiftForm(request.POST, instance=shift_info)

	    if form.is_valid():
                form.save()
                return redirect('attendance')

    context = {'shift_info':shift_info, 'form':form}
    return render(request, 'end_info.html', context)



def humanResource(request):
    shifts = Shift.objects.all()
    context = {'shifts':shifts}
    return render(request, 'report.html', context)