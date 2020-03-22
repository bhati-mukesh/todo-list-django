from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name="shopHome"),
    path('addtask', views.addtask,name="addtask"),
    path('testing/', views.testing,name="index"),
    path('taskdone/<int:id>', views.taskdone,name="index"),
    path('taskdelete/<int:id>', views.taskdelete,name="index"),

]