from django.shortcuts import redirect,render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method =='POST':
        listing_id = request.POST['listing_id']
        listings = request.POST['listing']
        name =request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id= request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_connected:
                #messages.info(request,'You have made enquiry already!')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing_id=listing_id,listings=listings,name=name,phone=phone,email=email,message=message,user_id=user_id)

        #send_mail
        send_mail(
            'Property Listing Inquiry',
            'There has been inquiry for' + listings +'.Sign into admin pannel for more info.',
            'ostigaurav9816@gmail.com',
            ['ostibhisma@gmail.com'],
            fail_silently=False
        )

        contact.save()
        #messages.info(request,'You have submitted your enquiry,realtors will contact you soon!')
        return redirect('/listings/'+ listing_id)
