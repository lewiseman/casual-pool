from django.shortcuts import render, redirect
from .forms import AddLeaveEducatorForm ,UpdateLeaveEducatorForm, UpdateLeaveManagerForm
from .models import Leaves
from django.core.mail import send_mail


def leave(request):
    educator = request.user.educator
    educator_leave = Leaves.objects.filter(educator=educator)
    form = AddLeaveEducatorForm(initial={'educator': educator})
    if request.method == 'POST':
        form = AddLeaveEducatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave')

    context = {'educator_leave':educator_leave, 'form':form}
    return render(request, 'leave.html', context)




def newLeave(request):
    leaves = Leaves.objects.all()
    context = {'leaves':leaves}
    return render(request, 'new_leave.html', context)


def UpdateLeaveEducator(request, pk):
    leave = Leaves.objects.get(id=pk)
    form = AddLeaveEducatorForm(instance=leave)

    if request.method == 'POST':
        form = AddLeaveEducatorForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave')

    context = {'form':form}
    return render(request, 'update_leave.html', context)




def UpdateLeaveManager(request, pk):
    leave_data = Leaves.objects.get(id=pk)
    form = UpdateLeaveManagerForm(instance=leave_data)

    if request.method == 'POST':
        form = UpdateLeaveManagerForm(request.POST, instance=leave_data)
        if form.is_valid():
            form.save()
            leave = UpdateLeaveManagerForm(request.POST)
            leave_status = leave['leave_status'].value()
            if leave_status == 'Approved':
                send_mail(
                        'Subject here',
                        'Approved.',
                        'from@example.com',
                        [leave_data.educator.user.email],
                        fail_silently=False,
                        )
            else :
                send_mail(
                        'Subject here',
                        leave_status,
                        'from@example.com',
                        [leave_data.educator.user.email],
                        fail_silently=False,
                        )
            return redirect('new_leave')

    context = {'form':form}
    return render(request, 'update_leave_manager.html', context)