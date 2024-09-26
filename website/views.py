from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.




def index(request): 
    if request.method == 'POST':
        service=request.POST.get('service')
        doctor=request.POST.get('doctor')
        patient_name=request.POST.get('patient_name')
        patient_email=request.POST.get('patient_email')
        date=request.POST.get('date')
        time=request.POST.get('time')

        send_mail(
            'Appointment Booked Successfully at DentCare',
            'Hello '+patient_name+',\n\nYour appointment for '+ service + ' has been booked successfully with '+doctor+' on '+date+' at '+time+'.\n\nThank You!',
            settings.EMAIL_HOST_USER,
            [patient_email],
            fail_silently=False,
        )

        messages.success(request, "Appointment Booked Successfully! Check your email for further details.")
        return render(request,'index.html',{})
    else:
        return render(request,'index.html',{})
