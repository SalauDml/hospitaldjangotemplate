from django.contrib import admin
from .models import DoctorInformation,HealthCareSolutions,AppointmentFormModel
# Register your models here.
admin.site.register(DoctorInformation)
admin.site.register(HealthCareSolutions)
admin.site.register(AppointmentFormModel)

