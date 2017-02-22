from django.shortcuts import render, redirect
from .models import Clothing
from .forms import ClothingForm

# Create your views here.

def index(request):
    closet = Clothing.objects.all()
    return render(request, 'clothes/index.html', {'closet' : closet})

def add(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClothingForm()
    return render(request, 'clothes/add.html', {'form' : form})
