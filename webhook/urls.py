from django.urls import path
from .views import alert_receiver, get_alerts, index, delete_entries

urlpatterns = [
    path('alert_receiver/', alert_receiver, name='alert_receiver'),
    path('api/alerts/', get_alerts, name='get_alerts'),
    path('', index, name='index'),
    path('delete_entries/', delete_entries, name='delete_entries'), 
]