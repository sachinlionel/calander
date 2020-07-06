from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from datetime import datetime, date, timedelta
import calendar
from django.views.generic import ListView, CreateView, DetailView
from django.utils.safestring import mark_safe
from .forms import EventForm

from .models import *
from .utils import Calendar

# Create your views here.


def home(request):
    return render(request, 'app/events.html')


class CalendarView(ListView):
    model = Event
    template_name = 'app/events.html'
    context_object_name = 'events'
    cal_year = None
    cal_month = None

    def get_context_data(self, **kwargs):

        if self.request.method == 'GET':
            print(self.request.GET)
            data = self.request.GET.get('month', None)
            if data:
                self.cal_year, self.cal_month = map(int, data.split('-'))

        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        if not self.cal_year and not self.cal_month:
            self.d = datetime.now()
            self.cal_year = self.d.year
            self.cal_month = self.d.month
        else:
            self.d = date(self.cal_year, self.cal_month, 1)

        # Instantiate our calendar class with today's year and date
        cal = Calendar(self.cal_year, self.cal_month, self.request.user)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = self.prev_month()
        context['next_month'] = self.next_month()
        return context

    def prev_month(self):
        first = self.d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
        return month

    def next_month(self):
        days_in_month = calendar.monthrange(self.d.year, self.d.month)[1]
        last = self.d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
        return month


class CalenderEventDetail(DetailView):
    model = Event
    template_name = 'app/event_detail.html'


class CalenderEventCreate(CreateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time', 'invitees']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

