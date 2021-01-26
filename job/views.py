from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from booking.forms import JobBookingForm
from django.core.mail import send_mail
from educator.models import Educator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def acceptJob(request, pk):
    job = Job.objects.get(id=pk)
    educator = request.user.educator
    form = JobBookingForm(initial={'educator':educator, 'status':'Accepted'}, instance=job)

    if request.method == "POST":
        form = JobBookingForm(request.POST)
        if form.is_valid():
            send_mail(
                'Petit Casual Pool: <educator> has accepted a booking on <date>',
                'booking_email.html',
                'from@example.com',
                   [job.manager.user.email],
                fail_silently=False,
                )
            form.save()
            job.delete()
            print("deleted")
            return redirect('/educator')

    context = {'item':job, 'form':form}

    return render(request, 'accept_job.html', context)



def createJob(request):
    manager = request.user.manager
    form = JobForm(initial={'manager': manager})
    educators = Educator.objects.all()
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job_details = JobForm(request.POST)
            job_date = job_details['date'].value()
            job_center = manager.centre
            job_from_time = job_details['shift_start_time'].value()
            job_to_time = job_details['shift_end_time'].value()
            msg_html = get_template('accept_job_email.html')
            a = { 'job_date': job_date, 'job_center':job_center, 'job_from_time':job_from_time, 'job_to_time':job_to_time}
            # for passing any values to the email in future 
            
            for educator in educators:
                subject, from_email= 'New job posted', 'harriet.ng.2020@gmail.com'
                to = educator.user.email
                html_content = msg_html.render(a)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            form.save()

            return redirect('manager_home')

    context = {'form':form}
    return render(request, 'create_job.html', context)



def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('/manager')

    context = {'form':form}
    return render(request, 'update_job.html', context)


def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == "POST":
        job.delete()
        return redirect('/manager')

    context = {'item':job}
    return render(request, 'delete_job.html', context)