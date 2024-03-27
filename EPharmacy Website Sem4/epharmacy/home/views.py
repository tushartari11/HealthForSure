from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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

# def generator(request):
#     if request.user.is_anonymous:
#         return redirect('/login')
#     return render(request, 'generator.html')

# def prescription(request):
#     return render(request, 'prescription.html')