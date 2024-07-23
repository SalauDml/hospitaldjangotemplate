from django import forms
from .models import AppointmentFormModel,DoctorInformation

class model_form(forms.ModelForm):
    class Meta:
        model = AppointmentFormModel
        fields = ['name','email','mobile','doctor','date','date2','problem']
        widgets= {
            'name':forms.TextInput(attrs = {'class': 'form-control border-0','placeholder':'Your Name',}),
            'email':forms.EmailInput(attrs = {'class': 'form-control border-0','placeholder':'Your Email'}),
            'mobile':forms.NumberInput(attrs = {'class': 'form-control border-0','placeholder':'Your Mobile'}),
            # 'doctor':forms.ModelChoiceField(queryset=DoctorInformation.objects.all(),to_field_name='doctor'),
            'date':forms.DateInput(attrs = {'class': 'form-control border-0 datetimepicker-input','placeholder':'Choose Date',}),
            'date2':forms.TimeInput(attrs = {'class': 'form-control border-0 datetimepicker-input','placeholder':'Choose Time'}),
            'problem':forms.Textarea(attrs={'class':'form-control border-0','placeholder':'Your Problem'})
        }

