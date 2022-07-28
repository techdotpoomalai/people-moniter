from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def system(request):
    return HttpResponse("this is system")