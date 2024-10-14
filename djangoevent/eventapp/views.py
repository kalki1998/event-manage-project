from django.shortcuts import render,redirect
from django.contrib import messages
from .models import event
from .forms import Bookingform
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        recipient_email = 'youremail@email.com'  # Change this to your email
    try:
        send_mail(
            'Contact Form Submission from ' + name,
            message + '\n\nFrom: ' + name + '\nEmail: ' + email,
            settings.EMAIL_HOST_USER,
            [recipient_email],  # use your email as the recipient and recieve emails from clients. 
            fail_silently=False
        )
        messages.success(request, 'Your email was sent successfully!')
    except Exception as e:
        messages.error(request, 'There was an error sending your email. Please try again later.')

    #note: change the EMAIL_HOST_USER,EMAIL_HOST_PASSWORD in settings.py, with your email and app password.
    return render(request,'contact.html')

def events(request):
    dict_eve ={
        'eve':event.objects.all()
    }
    return render(request,'events.html',dict_eve)

def booking(request):
    if request.method=='POST':
       form=Bookingform(request.POST) 
       if form.is_valid():
          form.save()
          return redirect('/')
    #access datas form booking models and store booking detalis to the database.
    form = Bookingform()
    dict_form ={
        'form':form
    }
    return render(request,'booking.html',dict_form)