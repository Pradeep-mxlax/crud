from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.views import View
from rest_framework.views import APIView
from .models import *
# from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PersonSerializer 
# from rest_framework import viewsets
# from rest_framework.pagination import PageNumberPagination
# Create your views here.
class index(APIView):
    def get(self,request):
         return render(request, 'login.html')
        # return HttpResponse("Test Successfull")
    
    def post(self,request):
         serializer = PersonSerializer(data=request.data)
         if serializer.is_valid(raise_exception=True):
              serializer.save()
         return render(request, 'login.html')
    
#     def delete(self,request,pk):
#          person = Person.objects.get(id=pk)
#          person.delete()
#          return redirect('register')
    
class Register(APIView):

     def get(self,request):
          datas = Person.objects.all()
          # paginator = PageNumberPagination()
          # result_page = paginator.paginate_queryset(datas, request)
          # print(result_page)
          # Serialize the paginated queryset
          serializer = PersonSerializer(datas, many=True)
          
          # Return paginated response
          # return paginator.get_paginated_response(serializer.data)
          return render(request,'register.html',{'users':serializer.data})
     
class Delete_user(APIView):
     def get(self,request):
          user_id = request.GET.get('user_id')
          Person.objects.filter(id=user_id).delete()

          return redirect('register')
          
class EditUser(APIView):
     def get(self,request,pk):
          # uid = request.GET.get('user_id')
          person = Person.objects.get(id=pk)
          print()
          return render(request,'edit.html',{'data':person})
     def post(self,request,pk):
          instance = Person.objects.get(id=pk)
          serializer = PersonSerializer(instance,data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return redirect('register')
