from django.shortcuts import render,get_object_or_404,redirect
# Http Imports
from django.http import HttpResponse
# Model Imports
from .models import Entry,Location
# Message Imports
from django.contrib import messages
# Date Imports
import datetime
# Login Imports
from django.contrib.auth.decorators import login_required
# Random imports
import string
import random
# Create your views here.
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

@login_required(login_url='/authenticate/login/')
def EntryData(request):
    location_names = Location.objects.all()
    if request.method == "POST":
        vehicle_no = request.POST["vehicle_no"]
        vehicle_type = request.POST["vehicle_type"]
        select_location = request.POST["select_location"]
        mobile = request.POST["mobile"]
        date = datetime.date.today()
        time = datetime.datetime.now().time()


        tag_number = random_char(2) + str(random_digits(4))
        location = Location.objects.get(location_name=select_location)

        if vehicle_type == "Four Wheeler":
            location.four_space -= 1
        if vehicle_type == "Three Wheeler":
            location.three_space -= 1
        else:
            location.two_space -= 1

        enter = Entry(location=location,vehicle_no=vehicle_no,vehicle_type=vehicle_type,mobile=mobile,tag_number=tag_number)
        enter.save()
        return render(request,'gateway/entry_details.html',context={'time':time,'vehicle_no':vehicle_no,'vehicle_type':vehicle_type,'mobile':mobile,'tag_number':tag_number,'date':date})
    return render(request,'gateway/entry.html',context={'ln':location_names})



@login_required(login_url='/authenticate/login/')
def Exit(request):
    location_names = Location.objects.all()
    if request.method == "POST":
        vehicle_no = request.POST["vehicle_no"]
        vehicle_type = request.POST['vehicle_type']
        tag_number = request.POST['tag_number']
        mobile = request.POST['mobile']
        select_location = request.POST["select_location"]
        location = Location.objects.get(location_name=select_location)
        if len(Entry.objects.filter(location=location,vehicle_no=vehicle_no,vehicle_type=vehicle_type,tag_number=tag_number,mobile=mobile)) == 1:
            obj = Entry.objects.filter(vehicle_no=vehicle_no,vehicle_type=vehicle_type,tag_number=tag_number)
            model = get_object_or_404(obj,pk=obj[0].pk)
            model.delete()
            messages.success(request, "Vehicle Is Present")
            return redirect('/gateway/exit/')
        else:
            messages.success(request, "No Data Found")
            return redirect('/gateway/exit/')
    return render(request,'gateway/exit.html',context={'ln':location_names})

@login_required(login_url='/authenticate/login/')
def Present_Vehicle(request):
    vehicles = Entry.objects.all()
    return render(request,'gateway/present_vehicles.html',context={'vehicles':vehicles})




