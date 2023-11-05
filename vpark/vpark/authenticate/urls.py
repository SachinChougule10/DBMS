from django.urls import path
from . import views

app_name= "authenticate"
urlpatterns = [
    path('login/',views.Login,name="login"),
    path('signup/',views.Signup,name="signup"),
    path("logout/",views.Logout,name="logout"),
    # Profile
    path('profile/<int:pk>/',views.my_profile,name="profile"),
    path('profile/edit/<int:pk>/',views.update_profile,name="edit_profile"),
    path('profile/password/<int:pk>/',views.ChangePassword,name="change_password"),
    path('profile/photo/<int:pk>/',views.ChangeProfilePhoto,name="change_profile_photo")
]