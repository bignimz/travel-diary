from django.test import TestCase
from .models import *

# Create your tests here.
class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.nairobi = Location.objects.create(name='Nairobi')
        self.travel = Category.objects.create(name='travel')
        self.fun = Category.objects.create(name='fun')

        self.drinks = Image.objects.create(
            name='adventure-safari', location=self.nairobi,  description='mountain climbing adventure')

        self.drinks.Category.add(self.travel)
        self.drinks.Category.add(self.fun)

    # def a testcase for instance of the drinks class
    def test_instance(self):
        self.drinks.save()
        self.assertTrue(isinstance(self.drinks, Image))

    def test_delete_image(self):
        self.drinks.save()
        self.drinks.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.drinks.save()
        self.drinks.name = 'MoreDrinks'
        self.assertTrue(self.drinks.name == 'MoreDrinks')

    def test_all_images(self):
        self.drinks.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)

    def test_search_by_category(self):
        self.drinks.save()
        images = Image.search_by_category('fun')
        self.assertTrue(len(images) > 0)

    def test_view_location(self):
        self.drinks.save()
        location = Image.view_location(self.nairobi)
        self.assertTrue(len(location) > 0)

    def test_view_category(self):
        self.drinks.save()
        categories = Image.view_category(self.music)
        self.assertTrue(len(categories) > 0)

class categoriesTest(TestCase):
    def setUp(self):
        self.adventure = Category(name='adventure')

    def test_instance(self):
        self.adventure.save()
        self.assertTrue(isinstance(self.adventure, Category))

class LocationTest(TestCase):
    def setUp(self):
        self.nairobi = Location(name='nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))