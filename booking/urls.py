from django.urls import path
from . import views
from .views import event_list, other_views
from .views.other_views import CalendarView, CalendarViewNew, DashBoard

urlpatterns = [
    path("calendar/", CalendarViewNew.as_view(), name="calendar"),
    path("calendars/", CalendarView.as_view(), name="calendars"),
    path("dashboard/", DashBoard.as_view(), name='dashboard-booking'),
    path("event/new/", views.other_views.create_event, name="event_new"),
    path("event/edit/<int:pk>/", views.other_views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.other_views.event_details, name="event-detail"),
    path("all-event-list/", views.event_list.AllEventsListView.as_view(), name="all_events"),
    path(
        "running-event-list/",
        views.event_list.RunningEventsListView.as_view(),
        name="running_events",
    ),
]