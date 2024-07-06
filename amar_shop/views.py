from django.shortcuts import render
from store.models import Product
import socket

def home(request):
    products = Product.objects.filter(is_available = True)
    pod = socket.gethostname()
    return render(request, 'index.html', {'products':products, 'pod':pod})
