from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def delete_location(self):
        self.delete()

    def save_location(self):
        self.save()

    

class Images(models.Model):
	descripton = models.TextField()
    location = models.ForeignKey(Location, null=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/', null = True)
    time = models.DateTimeField(auto_now_add=True, null=True)
   
    # category = models.ManyToManyField(categories)
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_title(cls, search_term):
        gallery = cls.objects.filter(descripton__icontains=search_term)
        return gallery