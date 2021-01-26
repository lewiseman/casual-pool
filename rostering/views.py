from django.shortcuts import render, redirect
from educator.models import Educator
from .forms import AddShiftForm

def rosterPage(request):
    work_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    educators = Educator.objects.all()

    form = AddShiftForm()
    if request.method == 'POST':
	    form = AddShiftForm(request.POST)
	    if form.is_valid():
                form.save()
                return redirect('roster')

    #baby = educators.room.get(room_name='Baby Room')
    context = {'educators':educators, 'form':form, 'work_days':work_days}
    return render(request, 'roster.html', context)
