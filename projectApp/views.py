import re
from django.shortcuts import render,redirect
from .models import *
from rest_framework.views import APIView
from .serializers import employessSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views import View

class employeeList(APIView):
    serializer_class = employessSerializer
    def get(self,request):
        employess1=employess.objects.all()
        serializer=employessSerializer(employess1,many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({"status_code": status.HTTP_200_OK, "message": "Everything is fine.", "data": data}, status=status.HTTP_200_OK)
        except:
            return Response({"status_code": status.HTTP_404_NOT_FOUND, "message": "You get something wrong"}, status=status.HTTP_404_NOT_FOUND)


# Create method
def create(request):
    if request.method == "POST":
        first = request.POST['first']
        last = request.POST['last']
        id = None
        obj = crud(id,first,last)
        obj.save()
        return redirect('/')
   
# Read method   
def read(request):
    try:
        obj = crud.objects.all()
    except crud.DoesNotExist:
        obj = None
    return render(request,'index.html',{'key':obj})

# Update method
def update(request,id):
    if request.method == "POST":
        first_name = request.POST['first']
        last_name = request.POST['last']
        obj1 = crud.objects.get(id=id)
        obj1.first = first_name
        obj1.last = last_name
        obj1.save()
        return redirect('/')
    else:
        try:
            obj = crud.objects.get(id=id)
        except crud.DoesNotExist:
            obj = None

        return render(request,'edit.html',{'key':obj})

# Delete method
def delete(request,id):
    try:
        obj = crud.objects.get(id=id)
    except crud.DoesNotExist:
        obj = None
    
    obj.delete()
    return redirect('/')


class HomeView(View):
    def get(self, request):
        context = {
            'emp_data' : employess.objects.all()
        }
        return render(request, "home.html",context)

    def post(self, request):
        if request.method=="POST":
            name = request.POST.get('name')
            phone = request.method.POST.get('number')
            sub = request.method.POST.get('sub')
            domain = request.method.POST.get('domain')
            address = request.method.POST.get('address')
            print(name,phone,)
            employess(name=name, phone=phone, sub=sub, domain=domain, address=address).save()

        return render(request, "home.html")