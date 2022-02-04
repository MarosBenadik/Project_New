from django.views.generic import ListView
from django.db.models import Q
from booking.models.event import Event


class AllEventsListView(ListView):
    """ All event list views """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.filter(Q(user=self.request.user) | Q(business=self.request.user))


class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.filter(Q(user=self.request.user) | Q(business=self.request.user))