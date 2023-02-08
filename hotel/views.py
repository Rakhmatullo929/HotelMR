from django.shortcuts import render


# Create your views here.

def base_index(request):
    return render(request, 'base_index.html')
