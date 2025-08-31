import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CarRequestForm
from django.contrib import messages
from .models import CarRequest

def index(request):
    return render(request, 'index.html')

def comprar(request):
    return render(request, 'comprar.html')


def dashboard(request):
    cars = CarRequest.objects.all().order_by('-id')  # newest first

    # Format total_price and monthly_payment as BRL
    for car in cars:
        car.total_price_brl = f"R$ {car.total_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        car.monthly_payment_brl = f"R$ {car.monthly_payment:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    return render(request, 'dashboard.html', {'cars': cars})

def dashboard(request):
    
    cars = CarRequest.objects.all().order_by('make')  # default sort by brand

    # Filters
    make_filter = request.GET.get('make')
    model_filter = request.GET.get('model')
    local_filter = request.GET.get('local')

    if make_filter:
        cars = cars.filter(make__icontains=make_filter)
    if model_filter:
        cars = cars.filter(model__icontains=model_filter)
    if local_filter:
        cars = cars.filter(local=local_filter)

    # Unique values for dropdowns
    makes = CarRequest.objects.values_list('make', flat=True).distinct().order_by('make')
    models = CarRequest.objects.values_list('model', flat=True).distinct().order_by('model')
    locals = CarRequest.objects.values_list('local', flat=True).distinct().order_by('local')

    context = {
        'cars': cars,
        'makes': makes,
        'models': models,
        'locals': locals,
        'selected_make': make_filter,
        'selected_model': model_filter,
        'selected_local': local_filter,
    }
    return render(request, 'dashboard.html', context)

def get_makes(request):
    url = "https://www.carqueryapi.com/api/0.3/"
    params = {
        "cmd": "getMakes",
        "sold_in_us": "1",
        "callback": ""  # Forces pure JSON output
    }
    r = requests.get(url, params=params)
    print('r', r, r.text[:500])

    try:
        data = r.json()  # Will work now because it's valid JSON
    except ValueError:
        return JsonResponse({"error": "Invalid response from CarQuery API"}, status=500)

    return JsonResponse(data)

# API to get models for a specific make
def get_models(request, make):
    url = "https://www.carqueryapi.com/api/0.3/"
    params = {
        "cmd": "getModels",
        "make": make,
        "sold_in_us": "1",
        "callback": ""
    }
    r = requests.get(url, params=params)

    try:
        data = r.json()
    except ValueError:
        return JsonResponse({"error": "Invalid response from CarQuery API"}, status=500)

    return JsonResponse(data)

def buy_car(request):
    if request.method == "POST":
        form = CarRequestForm(request.POST)
        if form.is_valid():
            form.save()  # no need to parse currency anymore

            # Show success message
            messages.success(request, "Carro salvo com sucesso!")

            # Redirect to the same form page for a new entry
            return redirect('comprar')
    else:
        form = CarRequestForm()  # fresh empty form

    return render(request, 'comprar.html', {'form': form})