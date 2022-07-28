from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def network(request):
    return HttpResponse("this is network")