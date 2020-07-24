from django.urls import path
from accounts import views

urlpatterns = [

path('',views.Home,name="home"),
path('register/',views.RegisterPage,name="register"),
path('login/',views.LoginPage,name="login"),
path('dashboard/',views.Dashboard,name="dashboard"),
path('logout/',views.LogOutUser,name="logout"),
path('update_profile/',views.ProfileUpdate,name="profile_update"),

]