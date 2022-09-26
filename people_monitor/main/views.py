from msilib import CreateRecord
from unittest import removeResult
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login as auth_login, logout
# from rest_framework import authentication

from .Serializer import Createuser_Serializer


# Create your views here.

@csrf_exempt
def Create_user(request):
    if request.method=='POST':
        request_data=JSONParser().parse(request)
        # print(request_data['username'])
        user=User.objects.create_user(request_data['username'], request_data['email'], request_data['password'])
        # user.first_name='sam'
        # user.last_name='hran'
        # user.is_active=False
        # user.is_staff=True
        user.is_superuser=True
        # user.save()
        return JsonResponse({"message":"Your register successfully...!"})

@csrf_exempt
def Login_user(request):
    if request.method=='POST':
        # request_data=JSONParser().parse(request)
        username='sai'
        password='12345'
        user1=authentication('sai')
        # print(user)
        if user1 is not None:
            # auth_login(request,user)
            return HttpResponse('user is authenticated')
        else:
            return HttpResponse('fail')

@csrf_exempt
def clean_all_data(request):
    User.objects.all().delete()
    return HttpResponse("Register table is cleaned...")


def main(request):
    return HttpResponse("This is main")

# @csrf_exempt
# def register(request):
#     if request.method=='POST':
#         new_data=JSONParser().parse(request)
#         data_seriazer=Register_Serializer(data=new_data)
#         if data_seriazer.is_valid():
#             data_seriazer.save()
#             return JsonResponse(data_seriazer.data,status=201)
#         return JsonResponse({"message":"Please enter proper data"},status=400)


