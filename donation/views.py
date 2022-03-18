from operator import add
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Donation

def donation(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    remarks = request.POST['remarks']
    user_id = request.POST['user_id']
    #pickup_date = request.POST['pickup_date']

    donation = Donation(name=name, email=email, phone=phone, address=address, remarks=remarks, user_id=user_id)

    donation.save()


    messages.success(request, 'Thank you for filling the donation form. Our representative shall get in touch soon.')
    return redirect('/organizations/')