from rest_framework import serializers
# from .models import Register
from .models import Create_user

# class Register_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Register
#         fields='__all__'

class Createuser_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Create_user
        fields='__all__'