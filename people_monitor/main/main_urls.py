from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('test', views.main),
    path('clean', views.clean_all_data),
    path('create_user', views.Create_user),
    path('login_user', views.Login_user),
]