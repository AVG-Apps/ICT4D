# from django.db import models
from django.db import models
# from django_mysql.models import ListCharField


class Fertilizer(models.Model):
    fertilizer_text = models.CharField(max_length=30)
    subdescription_text = models.CharField(max_length=20)
    description_text = models.CharField(max_length=400)
    # fertilizer_img_url = models.URLField(max_length=200)


    def __str__(self):
        return self.fertilizer_text

    # def add_description(self):
    #     return self.description_text
    #
    # def add_img_url(self):
    #     return self.fertilizer_img_url

class Crop(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    crop_text = models.CharField(max_length=30)
    # crop_img_url = URLField(max_length=200)

    def __str__(self):
        return self.crop_text

    # def add_img_url(self):
    #     return self.crop_img_url


class Weather(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    weather_text = models.CharField(max_length=30)
    # weather_img_url = URLField(max_length=200)

    def __str__(self):
        return self.weather_text

    # def add_img_url(self):
    #     return self.weather_img_url



