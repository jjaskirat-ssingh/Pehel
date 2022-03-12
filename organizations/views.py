from django.shortcuts import get_object_or_404, render

from .models import Organization

def index(request):
    organizations =  Organization.objects.order_by('-date_joined').filter(display=True)
    context = {
        'organizations': organizations
    }

    return render(request, 'pages/organizations.html', context) 

def organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)

    context = {
    'organization': organization
    }

    return render(request, 'pages/organization.html', context) 