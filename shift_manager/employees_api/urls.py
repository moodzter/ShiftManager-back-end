from django.urls import path 
from . import views 

urlpatterns = [
    path('api/employees', views.EmployeeList.as_view(), name='employee_list'),
    path('api/posts', views.PostList.as_view(), name="posts_list"),
    path('api/posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('api/employees/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'),
]