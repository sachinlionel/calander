from django.urls import path
from django.conf.urls import url
from .views import CalendarView, CalenderEventDetail, CalenderEventCreate


urlpatterns = [
    path('', CalendarView.as_view(), name='home'),
    # url(r'^event/new/$', event, name='event_new'),
    # url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('event/<int:pk>', CalenderEventDetail.as_view(), name='event-detail'),
    path('event/new', CalenderEventCreate.as_view(), name='event-create'),
]