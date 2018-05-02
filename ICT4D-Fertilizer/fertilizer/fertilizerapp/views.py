from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import FertilizerForm, CropForm, WeatherConditionForm
from .models import Fertilizer

#Index page
def index(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'fertilizerapp/index.html', context)

#Fertilizer page
def fertilizer(request, id=id):
    fertilizer = Fertilizer.objects.get(id=id)
    return render(request, 'fertilizerapp/detail.html', {'fertilizer': fertilizer})


#add new fertilizer
def add_fertilizer(request):
    if request.method == "POST":
        form = FertilizerForm(request.POST)
        if form.is_valid():
            fertilizer_item = form.save(commit=False)
            fertilizer_item.save()
            return redirect('/fertilizer/' + str(fertilizer_item.id) + '/')
    else:
        form = FertilizerForm()
    return render(request, 'fertilizerapp/fertilizer_form.html', {'form':form})

#edit fertilizer
def edit_fertilizer(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = FertilizerForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/fertilizer/' + str(item.id) + '/')
    return render(request, 'fertilizerapp/fertilizer_form.html', {'form':form})

#add new crop
def add_crop(request):
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            crop_item = form.save(commit=False)
            crop_item.save()
            return redirect('/add/crop/')
    else:
        form = CropForm()
    return render(request, 'fertilizerapp/crop_form.html', {'form':form})

#edit crop
def edit_crop(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = CropForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/fertilizer/' + str(item.id) + '/')
    return render(request, 'fertilizerapp/crop_form.html', {'form':form})


#add new weather
def add_weather(request):
    if request.method == "POST":
        form = WeatherConditionForm(request.POST)
        if form.is_valid():
            weather_item = form.save(commit=False)
            weather_item.save()
            return redirect('/add/weather/')
    else:
        form = WeatherConditionForm()
    return render(request, 'fertilizerapp/weather_form.html', {'form':form})

#edit weather
def edit_weather(request, id=None):
    item = get_object_or_404(Fertilizer, id=id)
    form = WeatherConditionForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/fertilizer/' + str(item.id) + '/')
    return render(request, 'fertilizerapp/weather_form.html', {'form':form})