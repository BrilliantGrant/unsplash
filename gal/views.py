from django.shortcuts import render,HttpResponse
from .models import Category,Location,Images

# Create your views here.
def index (request):
    images = Image.get_images()
    return render(request,'index.html',{"images":images})