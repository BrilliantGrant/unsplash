from django.test import TestCase
import datetime as dt
from .models import Images, Category, Location

# Create your tests here.
class ImagesTestClass(TestCase):

    def setUp(self):
        self.image = Images(image='imageurl', name='celebrity', descripton='Richest celebrity in world')

    def test_image_instance(self):
        self.assertTrue(isinstance(self.image, Images))

    def test_save_image_method(self):
        self.image.save_image()

        images = Images.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image_method(self):
        self.image.save_image()

        images = Images.objects.all()
        self.image.delete_image()

        images = Images.objects.all()
        self.assertTrue(len(images)==0)


class LocationTestClass(TestCase):

    def setUp(self):
        self.location = Location(name = 'Norway')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()

        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.location.save_location()

        locations = Location.objects.all()
        self.location.delete_location()

        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)



class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = category(name='people')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, category))

    def test_save_category_method(self):
        self.category.save_category()

        category_object = Category.objects.all()
        self.assertTrue(len(category_object)>0)

    def test_delete_category_method(self):
        self.category.save_category()

        category_object = Category.objects.all()
        self.category.delete_category()
        
        category_object = Category.objects.all()
        self.assertTrue(len(category_object)==0)


