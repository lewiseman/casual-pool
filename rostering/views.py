from django.shortcuts import render, redirect
from django.views.generic.dates import WeekArchiveView
from datetime import date, datetime
import calendar
from educator.models import Educator
from .forms import AddShiftForm
from .models import Shift, Holidays
from leave.models import Leaves
import calendar
from django.http import HttpResponse
from itertools import islice

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
    queryset = Shift.objects.all()
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True

    def data_row(self):
        week = self.kwargs['week']
        week_shift = Shift.objects.filter(date__week=week)
        first = date.fromisocalendar(2021,week,1)
        m = str(first)
        mn = m[-2:]
        mon = int(mn)
        dates = ['Mon', 'Tue', 'Wen', 'Thur', 'Fri']
        # for x in range(0,5):
        #     dates.append(mon)
        #     mon +=1

        staff_list = []
        for staff in week_shift:
            staff_list.append(staff.educator_shift.user.username)
        staff_set = set(staff_list)

        staff_dic = {}
        for sett in staff_set:
            staff_dic.update({sett : {dat:'' for dat in dates}})
        return staff_dic

    def date_filter(self, long_date):
        date_string = str(long_date)
        date_number = int(date_string[-2:])
        month_number = int(date_string[-5:-3])
        year_number = int(date_string[0:4])
        day_of_week = calendar.weekday(year_number,month_number,date_number)
        day_dic = {0:'Mon', 1:'Tue', 2:'Wen', 3:'Thur', 4:'Fri'}
        date_word = day_dic[day_of_week]
        return date_word

    def details(self, start, end, lunch):
        a = str(start)[0:-3]
        b = str(end)[0:-3]
        c = str(lunch)
        info = a + ' to ' + b + ' (L: ' + c + ' )'
        return info

    def data_items(self):
        week = self.kwargs['week']
        week_shift = Shift.objects.filter(date__week=week)
        holidays = Holidays.objects.filter(date__week=week)
        leaves = Leaves.objects.filter(date_from__week=week)
        first = date.fromisocalendar(2021,week,1)
        m = str(first)
        mn = m[-2:]
        mon = int(mn)
        dates = []
        for x in range(0,5):
            dates.append(mon)
            mon +=1
        data = self.data_row()

        for shift in week_shift:
            data[shift.educator_shift.user.username][self.date_filter(shift.date)] = self.details(shift.shift_start, shift.shift_end, shift.lunch)
            data[shift.educator_shift.user.username]['room'] = shift.educator_shift.room
            for holiday in holidays:
                #if self.date_filter(holiday.date) in dates:
                data[shift.educator_shift.user.username][self.date_filter(holiday.date)] = holiday.name
            for leave in leaves:
                data[leave.educator.user.username][self.date_filter(leave.date_from)] = 'Leave: ' + leave.leave_type
        return data


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
        context['weekly'] = self.data_items()
        context['all_staff'] = Educator.objects.all()
        return context

    def chunks(self, data, SIZE=10000):
        it = iter(data)
        for i in range(0, len(data), SIZE):
            yield {k:data[k] for k in islice(it, SIZE)}

    def add_date(self, no_date, year, week):
        day_dates = {'mon': 1, 'tue': 2,'wen':3, 'thu': 4, 'fri': 5}
        res = []
        for elem in no_date:
            x = str(next(iter(elem)))[0:3]
            day_of_week = day_dates[x]
            shift_date = date.fromisocalendar(year,week,day_of_week)
            elem['date'] = shift_date
            #res.append( first )
        
        first = date.fromisocalendar(2021,1,1)
        with_date = no_date
        return with_date

    def post(self, request, *args, **kwargs):
        shift_data = request.POST.dict()
        shift_data.pop('csrfmiddlewaretoken')
        shift_dic = {k: v for k, v in shift_data.items() if v}
        staff_username = shift_dic['staff_name']
        shift_dic.pop('staff_name')

        chunk_data = []
        if (len(shift_dic) % 3) == 0:
            chunk_data = [item for item in self.chunks(shift_dic, 3)]
        else:
            return HttpResponse(len(shift_dic) % 3)

        year = kwargs['year']
        full_data = self.add_date(chunk_data, kwargs['year'], kwargs['week'])
        name_instance = Educator.objects.all()
        for inst in name_instance:
            if inst.user.username == staff_username:
                print(inst.user.username)
                staff_id = inst.id

        for data in full_data:
            shift_db = Shift()
            shift_db.educator_shift = Educator.objects.get(id=staff_id)
            shift_db.date = data['date']
            shift_db.shift_start = list(data.values())[0] 
            shift_db.shift_end = list(data.values())[1]
            shift_db.lunch = list(data.values())[2]
            print( list(data.values()))
            shift_db.save()
        print(shift_data)
        return redirect(request.META.get('HTTP_REFERER', '/'))