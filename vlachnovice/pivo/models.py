from django.db import models
import math


class Settings(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    is_enabled = models.BooleanField(default=False)


class Brewery(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=255)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.brewery}'


class Tap(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    start = models.DateField()
    is_tapped = models.BooleanField(default=False)
    volume = models.IntegerField(default=50)
    price = models.IntegerField(default=0)

    def total_beers_in_keg(self):
        return self.volume * 2

    def raw_price_per_beer(self):
        return self.price / self.total_beers_in_keg()

    def price_per_beer(self):
        return 5 * math.ceil(self.raw_price_per_beer() / 5)

    def save(self, *args, **kwargs):
        if self.is_tapped:
            Tap.objects.update(is_tapped=False)
        super(Tap, self).save(*args, **kwargs)


class HomepageImage(models.Model):
    image = models.ImageField(upload_to="homepage_images")
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description or f"picture {self.pk}"

    @classmethod
    def get_random_image(cls):
        return cls.objects.order_by('?').first()
