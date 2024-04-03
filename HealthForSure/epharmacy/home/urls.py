from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('features', views.features, name='features'),
    path('addnewpatient', views.addNewPatient, name='addnewpatient'),
    path('viewexistingpatients', views.viewExistingPatients, name='viewexistingpatients'),
    path('deletepatient/<addnewpatient_id>', views.deletepatient, name='deletepatient'),
    path('patientinfo/<addnewpatient_id>', views.patientinfo, name='patientinfo'),
    path('gnrtprscrptn/<addnewpatient_id>', views.gnrtprscrptn, name='gnrtprscrptn'),
    path('generator', views.generator, name='generator'),
    path('prescription/<addnewpatient_id>', views.prescription, name='prescription')
]