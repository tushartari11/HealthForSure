from django.db import models

class Addnewpatient(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.fullname
    
class Medicine(models.Model):
    medname = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='home/images', default='')

    def __str__(self):
        return self.medname