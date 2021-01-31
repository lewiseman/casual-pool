from django.shortcuts import render, redirect
from django.views.generic.dates import WeekArchiveView
from datetime import date, datetime
import calendar
from educator.models import Educator
from .forms import AddShiftForm
from .models import Shift

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



class ShiftWeekArchiveView(WeekArchiveView):
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True

    def get_queryset(self):
        # will try normal queryset to see if it can work on default without week filter
        self.week = self.kwargs['week']
        return Shift.objects.filter(date__week=self.week)

    def week_header(self):
        week = self.kwargs['week']
        first = date.fromisocalendar(2021,week,1)
        m = str(first)
        mn = m[-2:]
        mon = int(mn)
        values = []
        for x in range(0,5):
            values.append(mon)
            mon +=1
        
        keys = ['Mon', 'Tue', 'Wen', 'Thur', 'Fri']
        week_day = dict(zip(keys, values))
        return week_day

    def get_context_data(self, **kwargs):
        week = self.kwargs['week']
        context = super().get_context_data(**kwargs)
        context['current_week'] = date.today().isocalendar()[1]
        context['current_year'] = datetime.now().year
        context['week_header'] = self.week_header()
        return context