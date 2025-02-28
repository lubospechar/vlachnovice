import math

from django.test import TestCase
from vlachnovice.pivo.models import Tap, Beer, Brewery


class TapModelTest(TestCase):
    def setUp(self):
        self.brewery = Brewery.objects.create(name="Test Brewery")
        self.beer = Beer.objects.create(name="Test Beer", brewery=self.brewery)
        self.tap = Tap.objects.create(
            beer=self.beer,
            start="2023-01-01",
            is_tapped=False,
            volume=50,
            price=100
        )

    def test_total_beers_in_keg(self):
        self.assertEqual(self.tap.total_beers_in_keg(), 100)

    def test_raw_price_per_beer(self):
        self.assertEqual(self.tap.raw_price_per_beer(), 1.0)

    def test_price_per_beer(self):
        self.assertEqual(self.tap.price_per_beer(), 5)

    def test_save_with_tapped_set_to_true(self):
        self.tap.is_tapped = True
        self.tap.save()
        self.assertTrue(self.tap.is_tapped)
        self.assertEqual(Tap.objects.filter(is_tapped=True).count(), 1)

    def test_save_with_tapped_set_to_false(self):
        self.tap.is_tapped = False
        self.tap.save()
        self.assertFalse(self.tap.is_tapped)

    def test_price_per_beer_rounding(self):
        self.tap.price = 333
        self.assertEqual(self.tap.price_per_beer(), 10)
