from django.shortcuts import render
from .models import Articles

def product_home(request):
    product = Articles.objects.all()
    return render(request, 'data/product_home.html', {'product': product})