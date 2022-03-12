from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    organization_id = request.POST['organization_id']
    organization = request.POST['organization']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    organization_email = request.POST['organization_email']

    #  Check if user has made inquiry already
    # if request.user.is_authenticated:
    #   user_id = request.user.id
    #   has_contacted = Contact.objects.all().filter(organization_id=organization_id, user_id=user_id)
    #   if has_contacted:
    #     messages.error(request, 'You have already made an inquiry for this organization')
    #     return redirect('/organizations/'+organization_id)

    contact = Contact(organization=organization, organization_id=organization_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    send_mail(
      'Organization Inquiry - Pehel',
      'There has been an inquiry for ' + organization + '. Sign into the admin panel for more info.',
      'pikachu.777.222@gmail.com',
      [organization_email, 'jjaskirat.ssingh@gmail.com'],
      fail_silently=False
    )

    messages.success(request, 'Your request has been submitted, an organization representative will get back to you soon.')
    return redirect('/organizations/'+organization_id)