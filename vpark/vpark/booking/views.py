from django.shortcuts import render,get_object_or_404,reverse,redirect
# Http Imports
from django.http import HttpResponse,HttpResponseRedirect
# Razorpay
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Login Imports
from django.contrib.auth.decorators import login_required
# Models Import
from .models import Location,Book
from authenticate.models import User_Signup
# Date Time Imports
import datetime


# Messages Import
from django.contrib import messages
# Create your views here.
@login_required(login_url='/authenticate/login/')
def RegisterLocation(request):
    if request.method == "POST" and request.FILES['myfiles']:
        location_name = request.POST["location_name"]
        location_address = request.POST["location_address"]
        four_space = request.POST["four_space"]
        two_space = request.POST["two_space"]
        three_space = request.POST["three_space"]
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        image = request.FILES['myfiles']

        location = Location(image=image,user=request.user,phone=phone,mobile=mobile,location_name=location_name,location_address=location_address,four_space=four_space,two_space=two_space,three_space=three_space)
        location.save()
        messages.success(request, "Location Stored Successfully")
        return redirect('/booking/register/location/')
    return render(request,'booking/register_location.html')

# This is just used as function

@login_required(login_url='/authenticate/login/')
def booking_info(request):
    return render(request,'booking/booking_info.html')


@login_required(login_url='/authenticate/login/')
def Booking(request,pk):
    location = get_object_or_404(Location, pk=pk)
    vehicle_type_four = Book.objects.filter(location=location, vehicle_type="four_wheeler", date=datetime.date.today())
    vehicle_type_two = Book.objects.filter(location=location, vehicle_type="two_wheeler", date=datetime.date.today())
    vehicle_type_three = Book.objects.filter(location=location, vehicle_type="three_wheeler", date=datetime.date.today())
    four_space = location.four_space
    two_space = location.two_space
    three_space = location.three_space
    user = get_object_or_404(User_Signup,pk=request.user.pk)
    # Cost var
    less_6 = 0
    more_6 = 0
    more_12 = 0
    amount = 0
    if request.method == "POST":
        vehicle_type = request.POST["vehicle_type"]
        vehicle_no = request.POST["vehicle_no"]
        date = request.POST["date"]
        start_time = request.POST["start_time"]
        end_time = request.POST["end_time"]
        slots = request.POST["slots"]

        # Cost
        start_time = datetime.time(int(start_time[0:2]), int(start_time[3:]), 0)
        stop_time = datetime.time(int(end_time[0:2]), int(end_time[3:]), 0)

        date = datetime.date(2021,5,4)
        datetime1 = datetime.datetime.combine(date, start_time)
        datetime2 = datetime.datetime.combine(date, stop_time)
        time = datetime1 - datetime2
        time = str(time)
        hour = int(time[8:10])
        minute = int(time[11:13])

        print(vehicle_type)
        cost = 0
        if (vehicle_type == "Four Wheeler"):
            if (datetime.time(hour,minute,00) <= datetime.time(hour=6, minute=0, second=0)):
                cost = 30
            if (datetime.time(hour,minute,00) >= datetime.time(hour=6, minute=0,
                                                       second=0) and datetime.time(hour,minute,00) <= datetime.time(hour=12,
                                                                                                            minute=0,
                                                                                                            second=0)):
                cost = 50
            if (datetime.time(hour,minute,00) >= datetime.time(hour=12, minute=0, second=0)):
                cost = 60
            else:
                cost = 10
        else:
            cost = 20


        if (vehicle_type == "Two Wheeler"):
            if (datetime.time(hour,minute,00) <= datetime.time(hour=6, minute=0, second=0)):
                cost = 15
            if (datetime.time(hour,minute,00) >= datetime.time(hour=6, minute=0,
                                                       second=0) and datetime.time(hour,minute,00) <= datetime.time(hour=12,
                                                                                                            minute=0,
                                                                                                            second=0)):
                cost = 25
            if (datetime.time(hour,minute,00) >= datetime.time(hour=12, minute=0, second=0)):
                cost = 30
            else:
                cost = 10
        else:
            cost = 20

        if (vehicle_type == "Three Wheeler"):
            if (datetime.time(hour,minute,00) <= datetime.time(hour=6, minute=0, second=0)):
                cost = 20
            if (datetime.time(hour,minute,00) >= datetime.time(hour=6, minute=0,
                                                       second=0) and datetime.time(hour,minute,00) <= datetime.time(hour=12,
                                                                                                            minute=0,
                                                                                                            second=0)):
                cost = 35
            if (datetime.time(hour,minute,00) >= datetime.time(hour=12, minute=0, second=0)):
                cost = 40
            else:
                cost = 10
        else:
            cost = 20

        # RazorPay
        amount = cost * 100
        client = razorpay.Client(
            auth=("rzp_test_C9CpGpkPwIljXs", "BbmSDpdc0g4Bz8eUQkVFd04a"))
        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})

        # Four Space
        # if booktime ends slot is made free for four_space.
        for i in range(len(vehicle_type_four)):
            if (vehicle_type_four[i].end_time >= datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()):
                vehicle_type_four[i].location.four_space += 1
        # if booktime ends slot is made free for four_space.
            if (vehicle_type_four[i].start_time >= datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()):
                vehicle_type_four[i].location.four_space -= 1

        # Two Space
        # if booktime ends slot is made free for two_space.
        for i in range(len(vehicle_type_two)):
            if (vehicle_type_two[i].end_time >= datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()):
                vehicle_type_two[i].location.two_space += 1
        # if booktime ends slot is made free for two_space.
            if (vehicle_type_two[i].start_time >= datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()):
                vehicle_type_two[i].location.two_space -= 1

        # Three Space
        # if booktime ends slot is made free for three_space.
        for i in range(len(vehicle_type_three)):
            if (vehicle_type_three[i].end_time >= datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()):
                vehicle_type_three[i].location.three_space += 1
        # if booktime ends slot is made free for three_space.
            if (vehicle_type_three[i].start_time >= datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()):
                vehicle_type_three[i].location.three_space -= 1

        # Booking
        if (vehicle_type == "Four Wheeler"):
            try:
                if (vehicle_type_four[0].location.four_space == 0):
                    messages.error(request,"No Space for Four Wheeler Left")
                    return redirect('/booking/book/'+str(pk))
                else:
                    book_space = Book(user=request.user,price=cost,location=location,vehicle_type=vehicle_type,vehicle_no=vehicle_no,date=date,start_time=start_time,end_time=end_time,slots=slots)
                    if location.four_space < int(slots):
                        messages.error(request, "No Space for Four Wheeler Left")
                        return redirect('/booking/book/' + str(pk))
                    else:
                        location.four_space = location.four_space - int(slots)
                        book_space.save()
                        return render(request,booking_info(request),
                                      context={"user":user,"vehicle_type_four": four_space - len(vehicle_type_four),
                                               "vehicle_type_two": two_space - len(vehicle_type_two),
                                               "vehicle_type_three": three_space - len(vehicle_type_three)
                                          , "cost": amount,"location":location,"vehicle_no":vehicle_no,"vehicle_type":vehicle_type
                                              ,'date':date,'in_time':start_time,'out_time':end_time})
            except:
                book_space = Book(user=request.user,price=cost, location=location, vehicle_type=vehicle_type,
                                  vehicle_no=vehicle_no, date=date, start_time=start_time, end_time=end_time,
                                  slots=slots)
                if location.four_space < int(slots):
                    messages.error(request, "No Space for Four Wheeler Left")
                    return redirect('/booking/book/' + str(pk))
                else:
                    location.four_space -= int(slots)
                    book_space.save()
                    return render(request, "booking/booking_info.html",
                                  context={"user":user,"vehicle_type_four": four_space - len(vehicle_type_four),
                                           "vehicle_type_two": two_space - len(vehicle_type_two),
                                           "vehicle_type_three": three_space - len(vehicle_type_three)
                                      , "cost": amount, "location": location, "vehicle_no": vehicle_no,
                                           "vehicle_type": vehicle_type
                                      , 'date': date, 'in_time': start_time, 'out_time': end_time})

        if (vehicle_type == "Two Wheeler"):
            try:
                if (vehicle_type_two[0].location.two_space == 0):
                    messages.error(request, "No Space for Two Wheeler Left")
                    return redirect('/booking/book/' + str(pk))
                else:
                    book_space = Book(user=request.user,price=cost, location=location, vehicle_type=vehicle_type,
                                      vehicle_no=vehicle_no, date=date, start_time=start_time, end_time=end_time,
                                      slots=slots)
                    if location.two_space < int(slots):
                        messages.error(request, "No Space for Two Wheeler Left")
                        return redirect('/booking/book/' + str(pk))
                    else:
                        location.two_space -= int(slots)
                        book_space.save()
                        return render(request, "booking/booking_info.html",
                                      context={"user":user,"vehicle_type_four": four_space - len(vehicle_type_four),
                                               "vehicle_type_two": two_space - len(vehicle_type_two),
                                               "vehicle_type_three": three_space - len(vehicle_type_three)
                                          , "cost": amount, "location": location, "vehicle_no": vehicle_no,
                                               "vehicle_type": vehicle_type
                                          , 'date': date, 'in_time': start_time, 'out_time': end_time})
            except:
                book_space = Book(user=request.user,price=cost, location=location, vehicle_type=vehicle_type,
                                  vehicle_no=vehicle_no, date=date, start_time=start_time, end_time=end_time,
                                  slots=slots)
                if location.two_space < int(slots):
                    messages.error(request, "No Space for Two Wheeler Left")
                    return redirect('/booking/book/' + str(pk))
                else:
                    location.two_space -= int(slots)
                    book_space.save()
                    return render(request, "booking/booking_info.html",
                                  context={"user":user,"vehicle_type_four": four_space - len(vehicle_type_four),
                                           "vehicle_type_two": two_space - len(vehicle_type_two),
                                           "vehicle_type_three": three_space - len(vehicle_type_three)
                                      , "cost": amount, "location": location, "vehicle_no": vehicle_no,
                                           "vehicle_type": vehicle_type
                                      , 'date': date, 'in_time': start_time, 'out_time': end_time})

        if (vehicle_type == "Three Wheeler"):
            try:
                if (vehicle_type_four[0].location.four_space == 0):
                    messages.error(request, "No Space for Three Wheeler Left")
                    return redirect('/booking/book/' + str(pk))
                else:
                    book_space = Book(user=request.user,price=cost, location=location, vehicle_type=vehicle_type,
                                      vehicle_no=vehicle_no, date=date, start_time=start_time, end_time=end_time,
                                      slots=slots)
                    if location.three_space < int(slots):
                        messages.error(request, "No Space for Three Wheeler Left")
                        return redirect('/booking/book/' + str(pk))
                    else:
                        location.three_space -= int(slots)
                        book_space.save()
                        return render(request, "booking/booking_info.html",
                                      context={"user":user,"vehicle_type_four": four_space - len(vehicle_type_four),
                                               "vehicle_type_two": two_space - len(vehicle_type_two),
                                               "vehicle_type_three": three_space - len(vehicle_type_three)
                                          , "cost": amount, "location": location, "vehicle_no": vehicle_no,
                                               "vehicle_type": vehicle_type
                                          , 'date': date, 'in_time': start_time, 'out_time': end_time})
            except:
                book_space = Book(user=request.user,price=cost, location=location, vehicle_type=vehicle_type,
                                  vehicle_no=vehicle_no, date=date, start_time=start_time, end_time=end_time,
                                  slots=slots)
                if location.three_space < int(slots):
                    messages.error(request, "No Space for Three Wheeler Left")
                    return redirect('/booking/book/' + str(pk))
                else:
                    location.three_space -= int(slots)
                    book_space.save()
                    return render(request, "booking/booking_info.html",
                                  context={"user":user,"vehicle_type_four": four_space - len(vehicle_type_four),
                                           "vehicle_type_two": two_space - len(vehicle_type_two),
                                           "vehicle_type_three": three_space - len(vehicle_type_three)
                                      , "cost": amount, "location": location, "vehicle_no": vehicle_no,
                                           "vehicle_type": vehicle_type
                                      , 'date': date, 'in_time': start_time, 'out_time': end_time})



    return render(request,'booking/booking.html',context={"location_name":location.location_name,"location_address":location.location_address,"phone":location.phone,"location_link":location.location_link,
                                                          "vehicle_type_four":four_space-len(vehicle_type_four),"vehicle_type_two":two_space-len(vehicle_type_two),"vehicle_type_three":three_space-len(vehicle_type_three)})

def SelectLocation(request):
    location = Location.objects.all()
    return render(request,"booking/select_location.html",context={"location":location})
