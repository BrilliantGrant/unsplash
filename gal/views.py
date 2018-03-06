from django.shortcuts import render,HttpResponse
from .models import Images

# Create your views here.
def index (request):
    images = Images.get_images()
    return render(request,'index.html',{"images":images})


def image(request, image_id):
    image = Images.objects.get(id=image_id)
    return render(request, 'image.html', {'image':image})


def search_results(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get('images')
        searched_image = Images.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images":searched_image})
    else:
        message = 'You haven\'t searched for any images.'
        return render(request, 'search.html', {"message":message})