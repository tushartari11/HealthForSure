from django.db import models

class Addnewpatient(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=20)
    medicines = models.CharField(max_length=200, default='Nothing')

    def __str__(self):
        return self.fullname