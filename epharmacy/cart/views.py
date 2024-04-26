from django.shortcuts import render, get_object_or_404
from .cart import Cart
from home.models import Medicine, Addnewpatient
from django.http import JsonResponse
import qrcode
from django.urls import reverse
import os

def viewcart(request, addnewpatient_id):
    cart = Cart(request)
    cart_products = cart.get_prods
    dandqs = cart.get_dandqs
    patientid = addnewpatient_id
    return render(request, 'viewcart.html', {'cart_products': cart_products, 'dandqs': dandqs, 'patientid': patientid})

def addcart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        productid = int(request.POST.get('product_id'))
        productdosage = request.POST.get('product_dosage')
        productquantity = int(request.POST.get('product_quantity'))

        product = get_object_or_404(Medicine, id=productid)
        cart.add(medicine=product, dosage=productdosage, quantity=productquantity)

        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response

def deletecart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        productid = int(request.POST.get('product_id'))
        cart.delete(product=productid) 

        response = JsonResponse({'productid': productid})
        return response
    
def finalprescription(request, addnewpatient_id):
    patient = Addnewpatient.objects.get(pk=addnewpatient_id)

    cart = Cart(request)
    cart_products = cart.get_prods
    dandqs = cart.get_dandqs
    total = cart.get_total
    patientid = addnewpatient_id

    return render(request, 'finalprescription.html', { 'fullname': patient.fullname, 'age': patient.age, 'gender': patient.gender, 'cart_products': cart_products, 'dandqs': dandqs, 'total': total, 'patientid': patientid})

def getqrcode(request, addnewpatient_id):
    # html_url = "http://127.0.0.1:8000/cart/finalprescription/"+addnewpatient_id
    html_url = "http://192.168.0.106:8000/cart/finalprescription/"+addnewpatient_id

    relative_path = "cart/static/"+addnewpatient_id+".png"
    abs_path = os.path.abspath(relative_path)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(html_url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(abs_path)

    return render(request, 'qrpage.html', {'addnewpatient_id': addnewpatient_id})