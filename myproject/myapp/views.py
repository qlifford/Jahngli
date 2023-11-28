from django.shortcuts import render, redirect
from .models import Product
from django.views import View
from .forms import CreateProductForm

def show_product(request):
    model = Product
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home/index.html', context)

def create_product(request):
    form = CreateProductForm()
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_products')
    return render(request, 'home/create.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = CreateProductForm(instance=product)
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = CreateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('show_products')
    return render(request, 'home/update.html', {'form': form})

def delete_product(request, id):
    model = Product
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('show_products')
