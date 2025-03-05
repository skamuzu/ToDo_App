from rest_framework import serializers
from .models import TodoItem

class ToDo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"
    
        
    