from django.shortcuts import render, redirect
from availability.models import Availability
from .forms import AvailabilityForm



def createAvailability(request):
    educator = request.user.educator
    form = AvailabilityForm(initial={'educator': educator})
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('educator_home')

    context = {'form':form}
    return render(request, 'add_availability.html', context)


    
def updateAvailability(request, pk):
    availability = Availability.objects.get(id=pk)
    form = AvailabilityForm(instance=availability)
    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('educator_home')
        else:
            print("not valid")

    context = {'form':form}
    return render(request, 'update_availability.html', context)


def deleteAvailability(request, pk):
    availability = Availability.objects.get(id=pk)
    if request.method == "POST":
        availability.delete()
        return redirect('educator_home')

    context = {'item':availability}
    return render(request, 'delete_availability.html', context)    