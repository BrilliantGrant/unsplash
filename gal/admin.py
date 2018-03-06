from django.contrib import admin
from .models import Location, Category,Images

# Register your models here.
class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal=('location','Category',)

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Images)
