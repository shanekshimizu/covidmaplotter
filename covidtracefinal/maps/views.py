from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

import datetime
from time import strftime
from .models import *
from .forms import *
from .filters import *
from .dataxml import *

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
        
    context = {'form':form}
    return render(request, 'maps/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'maps/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


    myFilter = PatientFilter(request.GET, queryset = patients)
    patients = myFilter.qs
  

    context = {
        'patients': patients,
        'locations': locations,
        'recent10locations': recent10locations,
        'recent10count': recent10count,
        'recent10patients': recent10patients, 'myFilter': myFilter,
        'patient_count': patient_count
    }
    return render(request, 'maps/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def doctor(request, pk_test):
    patient = Patient.objects.get(id=pk_test)
    locations = patient.locations.all()
    location_count = locations.count()

    myFilter = LocationFilter(request.GET, queryset = locations)
    locations = myFilter.qs

    context = {
        'patient': patient,
        'location_count': location_count, 
        'myFilter': myFilter,
        'locations':locations
    }
    return render(request, 'maps/doctor.html', context)


#-----Patient-----
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

    context = {
        'form': form,
        'form_name': form_name, 
    }
    return render(request, 'maps/patient_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    form_name = "Patient"
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        'form_name': form_name, 
    }
    return render(request, 'maps/patient_form.html', context)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form_name = "Patient"
    if request.method == "POST":
        patient.delete()
        return redirect('/')
    context = {
        'patient': patient,
        'form_name': form_name,
    }
    return render(request, 'maps/delete.html', context)

#-----Location-----#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

    context = {
        'form': form,
        'form_name': form_name,
    }
    return render(request, 'maps/patient_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateLocation(request, pk):
    location = Location.objects.get(id=pk)
    form = LocationForm(instance=location)
    form_name = "Location"

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form, 
        'form_name': form_name, 
    }
    return render(request, 'maps/patient_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteLocation(request, pk):
    location = Location.objects.get(id=pk)
    form_name = "Location"
    if request.method == "POST":
        location.delete()
        return redirect('/')

    context = {
        'location': location, 
        'form_name': form_name, 
    }
    return render(request, 'maps/delete.html', context)

def about(request):
    patients = Patient.objects.all()
    recent10patients = []
    patient_count = Patient.objects.count()
    new_cases = len(recent10patients)

    for patient in patients:
        if patient.date_created.strftime('%Y-%m-%d') == datetime.date.today():
            recent10patients.append(patient)
       

    context = {
        'patients': patients,
        'recent10patients': recent10patients,
        'patient_count': patient_count,
        'new_cases': new_cases,

    }
    return render(request, 'maps/about.html', context)