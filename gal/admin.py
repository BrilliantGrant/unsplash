from django.contrib import admin
from .models import Location, Category,Images

# Register your models here.
admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Images, ImagesAdmin)
