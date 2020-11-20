from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import *
from .dataxml import *
# Create your views here.
def home(request):
    patients = Patient.objects.all()
    locations = Location.objects.all()
    patient_count = Patient.objects.count()

    recent10patients = []
    recent10locations = []
    recent10count = {}
    for patient in patients:
        recent10patients.append(patient)
    for location in locations:
        recent10locations.append(location)
        recent10count[location.city] = Location.objects.filter(city=location.city).count()

    response = HttpResponse(open('maps/sample.xml').read(), content_type='application/xml')

    myFilter = PatientFilter(request.GET, queryset = patients)
    patients = myFilter.qs
  

    context = {'patients': patients, 'locations': locations, 'recent10locations': recent10locations, 'recent10count': recent10count, 'recent10patients': recent10patients, 'myFilter': myFilter, 'patient_count': patient_count}
    return render(request, 'maps/dashboard.html', context)

def doctor(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    locations = patient.locations.all()
    location_count = locations.count()

    myFilter = LocationFilter(request.GET, queryset = locations)
    locations = myFilter.qs

    context = {'patient': patient, 'location_count': location_count, 'myFilter': myFilter, 'locations':locations}
    return render(request, 'maps/doctor.html', context)


#-----Patient-----
def createPatient(request):
    '''
    Create Patient
    '''
    form = PatientForm()
    form_name = "Patient"
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'form_name': form_name, }
    return render(request, 'maps/patient_form.html', context)

def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    form_name = "Patient"
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'form_name': form_name, }
    return render(request, 'maps/patient_form.html', context)

def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form_name = "Patient"
    if request.method == "POST":
        patient.delete()
        return redirect('/')
    context = {'patient': patient, 'form_name': form_name, }
    return render(request, 'maps/delete.html', context)

#-----Location-----#
def createLocation(request):
    '''
    Create Location
    '''
    form = LocationForm()
    form_name = "Location"
   

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'form_name': form_name, }
    return render(request, 'maps/patient_form.html', context)


def updateLocation(request, pk):
    location = Location.objects.get(id=pk)
    form = LocationForm(instance=location)
    form_name = "Location"

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'form_name': form_name, }
    return render(request, 'maps/patient_form.html', context)

def deleteLocation(request, pk):
    location = Location.objects.get(id=pk)
    form_name = "Location"
    if request.method == "POST":
        location.delete()
        return redirect('/')
    context = {'location': location, 'form_name': form_name, }
    return render(request, 'maps/delete.html', context)


def about(request):
    

    response = HttpResponse(open('maps/sample.xml').read(), content_type='application/xml')
    return response
    return render(request, 'maps/about.html')