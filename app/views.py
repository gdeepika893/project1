from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def biryanizone(request):
    return HttpResponse('good biryani is available')