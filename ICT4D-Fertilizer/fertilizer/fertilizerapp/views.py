from django.http import HttpResponse
from django.template import loader

from .models import Fertilizer

def index(request):
    template = loader.get_template('fertilizerapp/index.html')
    return HttpResponse(template.render())


def detail(request):
    template = loader.get_template('fertilizerapp/detail.html')
    return HttpResponse(template.render())

def results(request):
    template = loader.get_template('fertilizerapp/results.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('fertilizerapp/addView.html')
    return HttpResponse(template.render())




# def add_fertilizer(fertilizer, crop, weather):
#     fertilizer_list = []
#
#     fertilizer.append({
#     'fertilizer': fertilizer,
#     'crop': crop,
#     'weather': weather})
