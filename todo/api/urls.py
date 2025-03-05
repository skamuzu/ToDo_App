from django.urls import path
from . import views


urlpatterns = [
    path('tasks/',views.task_list, name="Task List"), 
    path('tasks/<int:id>',views.task_item, name = "Task Item"),   
    path("test-view", view=views.TaskListCreateAPIView.as_view(), name="fuck bitch" )
]

