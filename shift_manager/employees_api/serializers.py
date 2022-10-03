from rest_framework import serializers 
from .models import Employee
from .models import Posts

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstName', 'lastName', 'age', 'title', 'pay',)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'name', 'subject', 'message',)