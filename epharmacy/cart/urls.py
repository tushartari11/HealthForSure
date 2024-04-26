from django.urls import path
from . import views

urlpatterns = [
    # path('', views.viewcart, name="viewcart"),
    path('viewcart/<addnewpatient_id>', views.viewcart, name='viewcart'),
    path('add/', views.addcart, name="addcart"),
    path('delete/', views.deletecart, name="deletecart"),
    path('finalprescription/<addnewpatient_id>', views.finalprescription, name="finalprescription")
]