from django.db import models
import math

class Settings(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    setting = models.BooleanField(default=False)

class Brewery(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Beer(models.Model):
    name = models.CharField(max_length=255)
    brewery = models.ForeignKey(Brewery, on_delete=models.Model)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.brewery}'

class Tap(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.Model)
    start = models.DateField()
    tap = models.BooleanField(default=False)
    volume = models.IntegerField(default=50)
    price = models.IntegerField(default=0)

    def beers_in_keg(self):
        return self.volume * 2

    def exact_price_per_beer(self):
        return self.price / self.beers_in_keg()

    def price_per_beer(self):
        return 5 * math.ceil(self.exact_price_per_beer() / 5)

    def save(self, *args, **kwargs):
        if self.tap==True:
            Tap.objects.update(tap=False)
        super(Tap, self).save(*args, **kwargs)
