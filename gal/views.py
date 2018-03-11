from django.shortcuts import render,HttpResponse
from .models import Images,Category
from django.template.context_processors import request

# Create your views here.
def index(request):
    image = Images.get_images()
    return render(request,'index.html',{"image":image})


def image(request, image_id):
    image = Images.objects.get(id=image_id)
    return render(request, 'image.html', {'image':image})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_category = Images.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "categories":searched_category})
    else:
        message = 'You haven\'t searched for any category.'
        return render(request, 'search.html', {"message":message})