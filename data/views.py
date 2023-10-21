from django.shortcuts import render

def product_home(request):
    return render(request, 'data/product_home.html')