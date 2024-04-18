from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_event, name='create_event'),
    path('update/<int:event_id>/', views.update_event, name='update_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('unregister/<int:event_id>/', views.unregister_event, name='unregister_event'),
    path('', views.event_list, name='event_list'),
    path('registered/', views.registered_events, name='registered_events'),
    path('reports/users/', views.user_list, name='user_list'),
    path('reports/events/', views.event_list_report, name='event_list_report'),
    path('reports/all-events/', views.all_events_report, name='all_events_report'),
    path('reports/event-registrants/<int:event_id>/', views.event_registrants_report, name='event_registrants_report'),
]
