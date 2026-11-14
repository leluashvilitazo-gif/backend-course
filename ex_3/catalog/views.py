from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

products = [
{"id": 1, "name": "Laptop", "price": 1800},
{"id": 2, "name": "Headphones", "price": 150},
{"id": 3, "name": "Mouse", "price": 40},
]

def home(request):
    return HttpResponse(
        '<h1>MyShop</h1><a href="/products">Products</a>'
    )

def about(request):
    return HttpResponse(
        '<h1>About me</h1><p>Im learning django!</p>'
    )

def product_list(request):
    items = "".join(f'<li><a href="/products/{p["id"]}/">{p["name"]} </a></li>'
        for p in products
    )

    return HttpResponse(f"<h1>Products</h1><ul>{items}</ul>")

def product_detail(request, pk):
    product = next(
        (p for p in products if p["id"] == pk),
        None
    )

    if product is None:
        raise Http404("product not found")

    return HttpResponse(
        f'<h1>{product["name"]}</h1><p>Price: ${product["price"]}</p>'
        )  