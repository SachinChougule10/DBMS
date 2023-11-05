from django.shortcuts import render,reverse,redirect,get_object_or_404

# Model Imports
from django.contrib.auth.models import User
from .models import User_Signup
from booking.models import Book
# Login Imports
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Message Import
from django.contrib import messages

# Http Imports
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

# Login
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not active")
        else:
            messages.error(request,"Username Or Password is Invaild")
            return redirect('/authenticate/login/')

    return render(request,'authenticate/login.html')

# Signup
def Signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            image = request.FILES.get('myfiles')
            new = User(first_name=first_name,last_name=last_name,email=email,username=username)
            new.set_password(password)
            new.save()             # Optional Information
            extra = User_Signup(image=image,user=new,phone=phone,address=address,age=age,mobile=mobile)
            extra.save()
            return HttpResponseRedirect('/authenticate/login/')
        except:
            new = User(first_name=first_name, last_name=last_name, email=email, username=username)
            new.set_password(password)
            new.save()  # Optional Information
            extra = User_Signup(user=new, phone=phone, address=address, age=age, mobile=mobile)
            extra.save()
            return HttpResponseRedirect('/authenticate/login/')

    return render(request,'authenticate/signup.html')

@login_required(login_url='/authenticate/login/')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/authenticate/login/')

@login_required(login_url='/authenticate/login/')
def my_profile(request,pk):
    if request.user.is_superuser:
        user = get_object_or_404(User,pk=pk)
        other_info = get_object_or_404(User_Signup,pk=user.user_content.pk)
        book = Book.objects.filter(user=pk)
        return render(request,'authenticate/MyProfile.html',context={'book':book,'user_info':user,'other_info':other_info})
    else:
        user = get_object_or_404(User, pk=pk)
        other_info = get_object_or_404(User_Signup,pk=user.user_content.pk)
        return render(request, 'authenticate/MyProfile.html',
                      context={'user_info': user,'other_info':other_info})

@login_required(login_url='/authenticate/login/')
def update_profile(request,pk):
    user_info = get_object_or_404(User,pk=request.user.pk)
    other_info = get_object_or_404(User_Signup, pk=user_info.user_content.pk)
    if request.method == "POST":
        username = request.POST['username']
        phone = request.POST["phone"]
        address = request.POST['address']
        mobile = request.POST['mobile']
        email = request.POST['email']

        # User model
        user_info.username = username
        user_info.email = email
        # Custom Model
        other_info.phone = phone
        other_info.address = address
        other_info.mobile = mobile

        user_info.save()
        other_info.save()

        return HttpResponseRedirect('/authenticate/profile/'+str(pk))


    return render(request,'authenticate/edit_profile.html',context={'user_info':user_info,'other_info':other_info})

@login_required(login_url='/authenticate/login/')
def ChangePassword(request,pk):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request,'Password does not matched')
            return redirect('/authenticate/login/')
        else:
            user.set_password(password)
            user.save()
    return render(request,'authenticate/change_password.html')

@login_required(login_url='/authenticate/login/')
def ChangeProfilePhoto(request,pk):
    user0 = get_object_or_404(User,pk=request.user.pk)
    user = get_object_or_404(User_Signup,pk=user0.user_content.pk)
    if request.method == "POST" and request.FILES['profile_image']:
        image = request.FILES['profile_image']
        user.image = image
        user.save()
        return redirect('/authenticate/profile/'+str(pk))
    return render(request,'authenticate/change_profile_photo.html')