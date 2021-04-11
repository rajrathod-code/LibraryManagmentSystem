from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class BookAPI(APIView):
    def get(self,request,format=None):
        if request.method == "GET":
            
            # retrived_data = AddBooks.objects.filter(category = 'Deploma')
            retrived_data = AddBooks.objects.all()
            serializer = AddBookSerializer(retrived_data,many=True)
            return Response(serializer.data)
        else:
            return Response({"msg" : "NOt Get request"})
    
    def post(self,request , format = None):
        if request.method == "POST":
            serializer = AddBookSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg" : "Data inserted successfully"})
            else:
                return Response(serializer.errors)

    def post(self,request , format = None):
        if request.method == "POST":
            serializer = RequestBookSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg" : "Data inserted successfully"})
            else:
                return Response(serializer.errors)

    def patch(self,request,pk=None , format = None):
        id = pk
        retrived_data = AddBooks.objects.get(book_id = id)
        serializer = AddBookSerializer(retrived_data , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : "Data updated successfully"})
        else:
            return Response(serializer.errors)



def index(request):
    return render(request,'index.html')