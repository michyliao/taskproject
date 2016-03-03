from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from task.models import Task
from task.serializers import TaskSerializer
from task.forms import TaskForm
import json

# Create your views here.
def home(request):
	form = TaskForm()
	return render(request, 'task/index.html', {'form' : form})


@api_view(['GET','POST'])
def task_collection(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
    	data = {
    		'title' : request.data.get('title'),
    		'description' : request.data.get('description')
    		} 
    	
    	serializer = TaskSerializer(data=data)
    	
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def task_element(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

