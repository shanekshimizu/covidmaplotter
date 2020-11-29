from django.contrib import admin
from .models import Patient, Doctor, Location, Hospital, Place
#Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Location)
admin.site.register(Hospital)
admin.site.register(Place)