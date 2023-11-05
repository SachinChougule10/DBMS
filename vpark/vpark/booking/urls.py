from django.urls import path
from . import views

app_name = "booking"
urlpatterns = [
    path('register/location/',views.RegisterLocation,name="register_location"),
    path('location/',views.SelectLocation,name="select_location"),
    path('book/<int:pk>/',views.Booking,name="booking"),
]