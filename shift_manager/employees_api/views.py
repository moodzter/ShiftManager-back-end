from rest_framework import generics 
from .serializers import EmployeeSerializer
from .serializers import PostSerializer
from .models import Employee
from .models import Posts 
# Create your views here.

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all().order_by('id')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all().order_by('id')
    serializer_class = PostSerializer