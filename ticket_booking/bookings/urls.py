from django.urls import path
from .views import EventList, EventDetail, TicketList, TicketDetail

urlpatterns = [
    path('events/', EventList.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('tickets/', TicketList.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket_detail'),
]