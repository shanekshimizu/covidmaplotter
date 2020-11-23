from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
