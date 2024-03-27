from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('features', views.features, name='features'),
    # path('generator', views.generator, name='generator'),
    # path('prescription', views.prescription, name='prescription')
]