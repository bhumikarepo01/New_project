from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import AttendeeForm


# List all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


# Event detail + registration
def event_detail(request, pk):
    event = get_object_or_404(Event, id=pk)
    form = AttendeeForm(request.POST or None)

    if form.is_valid():
        attendee = form.save(commit=False)
        attendee.event = event
        attendee.save()
        return redirect('event_detail', pk=pk)

    return render(request, 'event_detail.html', {
        'event': event,
        'form': form,
        'attendees': event.attendees.all()
    })