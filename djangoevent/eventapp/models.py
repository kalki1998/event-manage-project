from django.db import models

# Create your models here.
class event(models.Model):
    img = models.ImageField(upload_to='uploads')
    name = models.CharField(max_length=50)
    desc = models.TextField()
    def __str__(self):
        return self.name

class booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    event_name = models.ForeignKey(event,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

   