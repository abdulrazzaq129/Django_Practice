from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.contrib.auth.models import User
def home(request):
    return render(request,'home.html')

def product_detail(request,product_name):
    return HttpResponse(f"Hi, welcom to product detail with {product_name}")

def article(request,year):
    return HttpResponse(f"Article from the year {year}")
@api_view(['GET'])
def article_detail(request,**kwargs):
    return HttpResponse(f"Article from the year {kwargs}")

@api_view(['POST'])
def reverse_words(request):
    text = request.data.get('text')
    count = 0
    for word in text.split():
        count = count + 1
    
    return Response(count)

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializers = StudentSerializer(students,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

@api_view(['GET','PUT','DELETE'])
def student_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error":"Student does not exist"},status=404)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        student.delete()
        return Response(f"Deleted student with id {id} with name {student.name}")

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.create_user(username=username,password=password)
    user.is_superuser = True
    user.email = username
    user.save()
    return Response({"message":"User created"})

from django.contrib.auth import authenticate

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username,password=password)
    if user is not None:
        return Response({"message":"User authenticated"})
    return Response({"message":"User not authenticated"})
@api_view(['PATCH'])
def partial_update(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error":"Student does not exist"},status=404)
    if request.method == 'PATCH':
        serializers = StudentSerializer(student, data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
@api_view(['GET'])
def age_filter(request):
    student = Student.objects.filter(age__gt=20)
    serializers = StudentSerializer(student, many=True)
    return Response(serializers.data)
    


