# from django.db import models
from django.db.models import CharField, Model
# from django_mysql.models import ListCharField


class Fertilizer(Model):
    fertilizer_text = CharField(max_length=30)

    def __str__(self):
        return self.fertilizer_text

class Crop(Model):
    crop_text = CharField(max_length=30)

    def __str__(self):
        return self.crop_text


class Weather(Model):
    weather_text = CharField(max_length=30)

    def __str__(self):
        return self.weather_text



