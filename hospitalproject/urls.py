"""
URL configuration for hospitalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hospitalapp.views import home_page_view,about_page_view,appointment_page_view,contact_page_view,feature_page_view,service_page_view,team_page_view,testimonial_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page_view,name='home'),
    path('about/',about_page_view,name='about'),
    path('appointment/',appointment_page_view,name='appointment'),
    path('contact/',contact_page_view,name='contact'),
    path('feature/',feature_page_view,name='feature'),
    path('service/',service_page_view,name='service'),
    path('team/',team_page_view,name='team'),
    path('testimonial/',testimonial_page_view,name='testimonial'),    
]
urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
