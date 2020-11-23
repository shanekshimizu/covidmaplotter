from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('doctor/<str:pk_test>/', views.doctor, name="doctor"),
    path('about/', views.about, name="about"),
    path('create_patient', views.createPatient, name="create_patient"),
    path('update_patient/<str:pk>/', views.updatePatient, name="update_patient"),
    path('delete_patient/<str:pk>/', views.deletePatient, name="delete_patient"),
    path('create_location', views.createLocation, name="create_location"),
    path('update_location/<str:pk>/', views.updateLocation, name="update_location"),
    path('delete_location/<str:pk>/', views.deleteLocation, name="delete_location"),

]