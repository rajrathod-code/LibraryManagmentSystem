from rest_framework import serializers
from .models import *

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBooks
        fields = '__all__'

class RequestBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestBook
        fields = '__all__'