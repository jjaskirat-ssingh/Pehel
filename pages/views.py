from django.shortcuts import render

# from team.models import Member
# from events.models import Event

def index(request):
    # members = Member.objects.all().filter(in_office=True)
    # events = Event.objects.all().filter(display=True)

    # context = {
    #     'members': members,
    #     'events': events
    # }

    return render(request, 'pages/index.html')#, context)

def about(request):
    return render(request, 'pages/about.html')