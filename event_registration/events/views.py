from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm
from django.utils import timezone

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', {'event': event})

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.registrants.add(request.user)
        return redirect('event_list')
    return render(request, 'register_event.html', {'event': event})

@login_required
def unregister_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.registrants.remove(request.user)
        return redirect('event_list')
    return render(request, 'unregister_event.html', {'event': event})

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def registered_events(request):
    events = request.user.registered_events.all()
    return render(request, 'registered_events.html', {'events': events})

@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def event_list_report(request):
    events = Event.objects.filter(end_date__gte=timezone.now())
    return render(request, 'event_list_report.html', {'events': events})

@login_required
@user_passes_test(is_admin)
def all_events_report(request):
    events = Event.objects.all()
    return render(request, 'all_events_report.html', {'events': events})

@login_required
@user_passes_test(is_admin)
def event_registrants_report(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registrants = event.registrants.all()
    return render(request, 'event_registrants_report.html', {'event': event, 'registrants': registrants})
