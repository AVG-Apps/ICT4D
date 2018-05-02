from django.forms import ModelForm
from .models import Fertilizer, Crop, Weather

class FertilizerForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['fertilizer_name', 'description', 'subdescription', 'weather_condition_list', 'crop_list']

        # fields = '__all__'
        # exclude = ['fertilizer']

class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = ['crop_name', 'crop_img_url']


class WeatherConditionForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['weather_condition']
