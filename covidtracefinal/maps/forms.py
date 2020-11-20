from django.forms import ModelForm
from .models import *

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