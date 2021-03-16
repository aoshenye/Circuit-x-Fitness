from django.shortcuts import render

# Create your views here.
def Ptrainers(request):
    return render(request, 'products/trainers.html')