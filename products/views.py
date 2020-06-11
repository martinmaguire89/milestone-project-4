from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'my_app/products.html', {'filter': f})
