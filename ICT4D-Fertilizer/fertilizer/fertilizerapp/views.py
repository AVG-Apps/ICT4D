from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render




from .models import Fertilizer, Crop, Weather

def index(request):
    latest_fertilizer_list = Fertilizer.objects.all()
    context = {'latest_fertilizer_list': latest_fertilizer_list}
    return render(request, 'fertilizerapp/index.html', context)


def detail(request, fertilizer_id):
    fertilizer = get_object_or_404(Fertilizer, pk=fertilizer_id)
    return render(request, 'fertilizerapp/detail.html', {'fertilizer': fertilizer})

def edit(request, fertilizer_id):
    fertilizer = get_object_or_404(Fertilizer, pk=fertilizer_id)
    return render(request, 'fertilizerapp/edit.html', {'fertilizer': fertilizer})

def results(request, fertilizer_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % fertilizer_id)

def add(request):
    template = loader.get_template('fertilizerapp/addView.html')
    return HttpResponse(template.render())
