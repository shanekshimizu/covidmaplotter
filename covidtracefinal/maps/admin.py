from django.contrib import admin
from .models import Patient, Doctor, Location, Hospital
#Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Location)
admin.site.register(Hospital)