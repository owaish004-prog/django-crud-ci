from django.shortcuts import render, redirect
from .models import Product
# import Beautifulsoap
def product_list(request):
    return render(request,'list.html',{'products':Product.objects.all()})
def create_product(request):
    if request.method=='POST':
        Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price')
        )
    return redirect('/')
