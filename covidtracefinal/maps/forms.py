from django.forms import ModelForm, Select
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from location_field.forms.plain import PlainLocationField


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = 'address', 'latitude', 'longitude', 'city', 'loc_type', 'cooldown'
       

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'