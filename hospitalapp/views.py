from django.shortcuts import render,redirect
from .models import DoctorInformation,AppointmentFormModel,HealthCareSolutions
from .forms import model_form

# Create your views here.
def home_page_view(request):
    service = HealthCareSolutions.objects.all()
    doctors_info = DoctorInformation.objects.all()
    form = model_form()
    context={
        'services':service,
        'doctors':doctors_info,
        'form':form,
    }
    if request.method == 'POST':
        form_data = model_form(request.POST)
        if form_data.is_valid():
            form_data = form_data.save()
            # form_data= form_data.save()
            return redirect('home')

    return render(request,"main/index.html",context)
def about_page_view(request):
    doctors_info=DoctorInformation.objects.all()
    context={
        'doctors':doctors_info
    }
    return render(request,"main/about.html",context)
def appointment_page_view(request):
    return render(request,"main/appointment.html")
def contact_page_view(request):
    return render(request,"main/contact.html")
def feature_page_view(request):
    return render(request,"main/feature.html")
def service_page_view(request):
    service = HealthCareSolutions.objects.all()
    context={
        'services':service
    }
    return render(request,"main/service.html",context)
def team_page_view(request):
    return render(request,"main/team.html")
def testimonial_page_view(request):
    return render(request,"main/testimonial.html")

