from django.shortcuts import render,redirect
from .models import Contacts
from django.contrib import messages
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']
        message=request.POST['message']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contacts.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an inquery for this listing.")
                return redirect("/listings/"+str(listing_id))

        cont=Contacts(listing_id=listing_id,message=message,listing=listing,name=name,email=email,phone=phone,user_id=user_id)
        cont.save()
        
        subject, from_email, to = 'Property Listing Inquery', 'moin26944@gmail.com', [realtor_email]
        text_content = ""
        html_content = f"""There has been inquery for {listing}. Please sign to the admin panel for more info.<br>
        <strong>User ID: </strong>{user_id}<br>
        <strong>Name: </strong>{name}<br>
        <strong>Phone: </strong>{phone}<br>
        <strong>Message: </strong><br>{message}"""
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        # send_mail(
        #     "Property Listing Inquery",
        #     # "There has been inquery for "+listing+". Please sign to the admin panel for more info.\n",
        #     from_email= "moin26944@gmail.com",
        #     recipient_list=[realtor_email,'akmalk080@gmail.com'],
        #     fail_silently=False,
        #     html_message=["<h2>Message:</h2>\n"+message]
        # )

        messages.success(request,"Your requset is submited, a realtor will get back you soon")
        return redirect("/listings/"+str(listing_id))
        
    return render(request,"listings/listings.html")
 
