from django.shortcuts import render,reverse

# Mail Imports
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Model Imports
from authenticate.models import Contact


# IndexView
def indexview(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        s = Contact(name=name,email=email,subject=subject,message=message)
        s.save()
    return render(request,'index.html')

