import django_filters

from .models import *

class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = '__all__'
        

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = '__all__'