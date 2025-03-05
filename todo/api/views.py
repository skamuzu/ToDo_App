from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import TodoItem
from .serializers import ToDo_Serializer

from rest_framework.generics import ListCreateAPIView

class TaskListCreateAPIView(ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = ToDo_Serializer
    
    



# Create your views here.
@api_view(["GET","POST"])
def task_list(request, format = None):
    
    if request.method == "GET":
        todo_list = TodoItem.objects.all()
        serializer = ToDo_Serializer(todo_list, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ToDo_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(["GET","PUT","PATCH","DELETE"])
def task_item(request, id, format = None):
    try:
        task = TodoItem.objects.get(pk = id)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = ToDo_Serializer(task)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ToDo_Serializer(task, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PATCH":
        serializer = ToDo_Serializer(task, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    