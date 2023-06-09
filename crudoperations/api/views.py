from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Data
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def show(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id',None)
        if id is not None:
            stu = Data.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        
        stu = Data.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res = {'mes':'your data has been saved successfully.'}
            return JsonResponse(res)
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id')
        stu = Data.objects.get(id = id)
        serializer = StudentSerializer(stu,data=parsed_data,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'mes':'your data has been updated  successfully.'}
            return JsonResponse(res)
        
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id')
        stu = Data.objects.get(id = id)
        stu.delete()
        res = {'mes':'your data has been delete  successfully.'}
        return JsonResponse(res)
    

    