from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

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
    except:
        return Response(status = 404)
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

