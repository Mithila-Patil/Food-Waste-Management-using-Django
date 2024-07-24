from django.shortcuts import render, redirect
from .models import Donor, Receiver, FoodDonor

def index(request):
    return render(request, 'index.html')

def donor(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        city = request.POST.get('city')
        password = request.POST.get('pass')
        Donor.objects.create(user_id=user_id, city=city, password=password)
    return render(request, 'donor.html')

def receiver(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        city = request.POST.get('city')
        password = request.POST.get('pass')
        Receiver.objects.create(user_id=user_id, city=city, password=password)
    return render(request, 'receiver.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def foodid(request):
    return render(request, 'foodid.html')

def formdonor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        food_info = request.POST.get('food_info')
        quantity = request.POST.get('quantity')
        pick_up_date = request.POST.get('pick_up_date')
        FoodDonor.objects.create(
            name=name, city=city, phone=phone, address=address, food_info=food_info, 
            quantity=quantity, pick_up_date=pick_up_date
        )
    return render(request, 'formdonor.html')

def dashboard(request):
    donations = FoodDonor.objects.all()
    return render(request, 'dashboard.html', {'data': donations})