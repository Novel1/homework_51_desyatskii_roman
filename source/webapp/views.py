from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Category, Product


# Create your views here.

def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products_view.html', context=context)


def add_product(request):
    if request.method == 'GET':
        context = {'categories': Category.objects.all()}
        return render(request, 'add_product.html', context=context)
    product = {
        'name': request.POST.get('name'),
        'category': get_object_or_404(Category, name=request.POST.get('category')),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'image': request.POST.get('image'),
    }
    products = Product.objects.create(**product)
    return redirect('product_view', pk=products.pk)


def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'add_category.html')

    category = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
    }
    Category.objects.create(**category)
    return redirect('products_view')


def product_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponseNotFound('No Found')
    return render(request, 'inform_products.html', context={
        'product': product
    })
