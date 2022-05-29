from django.shortcuts import render, HttpResponse
# from .models import Image
from django.db.models import Q, query



def index(request):

    return render(request, 'index.html')