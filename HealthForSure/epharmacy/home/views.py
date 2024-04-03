from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import Addnewpatientform
from .models import Addnewpatient

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def loginUser(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/features')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def features(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'features.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

def addNewPatient(request):
    if request.method == 'POST':
        form = Addnewpatientform(request.POST or None)
        if form.is_valid():
            form.save()
            patient = Addnewpatient.objects.last()
            return render(request, 'generator.html', {'patient': patient}) 
        return render(request, 'addnewpatient.html') 
    else:
        return render(request, 'addnewpatient.html') 

def viewExistingPatients(request):
    patients = Addnewpatient.objects.all
    return render(request, 'viewexistingpatients.html', {'patients': patients})

def deletepatient(request, addnewpatient_id):
    p = Addnewpatient.objects.get(pk=addnewpatient_id)
    p.delete()
    return redirect('/viewexistingpatients')

def patientinfo(request, addnewpatient_id):
    patient = Addnewpatient.objects.get(pk=addnewpatient_id)
    return render(request, 'patientinfo.html', {'patient': patient})

def gnrtprscrptn(request, addnewpatient_id):
    patient = Addnewpatient.objects.get(pk=addnewpatient_id)
    return render(request, 'generator.html', {'patient': patient})

def generator(request):
    return render(request, 'generator.html')

def prescription(request, addnewpatient_id):
    patient = Addnewpatient.objects.get(pk=addnewpatient_id)
    return render(request, 'prescription.html', { 'fullname': patient.fullname, 'age': patient.age, 'gender': patient.gender })