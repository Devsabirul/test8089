import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import ProductDetails
from .forms import ProductForm
# Create your views here.


def home(request):
    product_details = ProductDetails.objects.all()
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        fm.save()
    fm = ProductForm()
    l = len(product_details)

    context = {
        'product_details': product_details,
        'form': fm,
        'length': l
    }

    return render(request, 'home/index.html', context)


def delete(request):
    data = request.POST
    id = data.get('id')
    prod_d = ProductDetails.objects.get(id=id)
    prod_d.delete()
    return redirect('/')


def update(request, id):
    if request.method == 'POST':
        data = ProductDetails.objects.get(id=id)
        fm = ProductForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    data = ProductDetails.objects.get(id=id)
    fm = ProductForm(instance=data)
    return render(request, 'home/update.html', {'form': fm})
