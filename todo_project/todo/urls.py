from django.urls import path
from .views import ListTodo, DetailsTodo

urlpatterns = [
    path('', ListTodo.as_view(), name='list'),
    path('<int:pk>/', DetailsTodo.as_view(), name='details')

]