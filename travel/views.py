from django.shortcuts import render, HttpResponse
from .models import Image
from django.db.models import Q, query



def index(request):
    travel = Image.objects.all()
    return render(request, 'index.html', {'travel': travel})


def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_images = request.GET.get("category")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})