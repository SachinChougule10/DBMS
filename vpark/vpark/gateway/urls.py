from django.urls import path
# Views import
from . import views

app_name = 'gateway'
urlpatterns = [
    path('entry/',views.EntryData,name="entry"),
    path('exit/',views.Exit,name="exit"),
    path('present/',views.Present_Vehicle,name="present"),
]