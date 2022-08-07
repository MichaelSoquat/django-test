from django.shortcuts import render
from .models import Cars

# Create your views here.
def renderContentView(request):
    cars = Cars.objects.all()
    return render(request, 'render.html', {'cars': cars})
