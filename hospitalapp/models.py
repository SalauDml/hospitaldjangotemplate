from django.db import models

# Create your models here.
class HealthCareSolutions(models.Model):
    icon= models.CharField(max_length=50,default="asgkl;;")
    category= models.CharField(max_length=50)
    text= models.TextField()
    seconds= models.CharField(max_length=10,null=True,default=True)
   
    def __str__(self) -> str:
        return self.category
    
class DoctorInformation(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    image= models.ImageField(upload_to="doctorimages",null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class PatientTestimonial(models.Model):
    image= models.ImageField(upload_to="patientimages",null=True,blank=True)
    name= models.CharField(max_length=50)
    profession= models.CharField(max_length=50)
    text=models.TextField()

    def __str__(self) -> str:
        return self.name
    

class AppointmentFormModel(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    doctor= models.ForeignKey(DoctorInformation,on_delete=models.SET_DEFAULT, default=1)
    date = models.DateField()
    date2= models.TimeField()
    problem = models.TextField()
    
    def __str__(self) -> str:
        return self.name
        