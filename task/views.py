from .models import User,Task
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import datetime

def index(request):
    return render(request,'index.html',{'tasks':getTasks(1),'ctasks':Task.objects.filter(userId=1,complete="yes")})

def addtask(request):
    tsk = request.POST.get('task',default="default").strip()
    print(type(tsk))
    if tsk == '':
        return HttpResponseRedirect('/')
    Task(task=tsk,publishedDate=datetime.datetime.now(),priority=1,doneToBeDate=datetime.datetime.now(),userId=1,complete='no').save()
    print(tsk)
    return HttpResponseRedirect('/')

def taskdone(request, id):
    user = Task.objects.filter(taskID=id,complete='no')[0]
    user.complete="yes"
    user.save()
    print(user.complete)
    return HttpResponseRedirect('/')

def taskdelete(request, id):
    print(id)
    return HttpResponseRedirect('/')
# ------ For Testing purpose -------

def testing(request):
    d = Task.objects.filter(taskID=3)[0]
    print(d.task)
    # d.complete="yes"
    # d.save()
    # print(d.complete)
    # getTasks(1)
    return render(request,'testing.html')

# ------- Custom function -------
def getTasks(userId):
    all_user = Task.objects.filter(userId=userId,complete='no')
    # print(all_user)
    # print(len(all_user))
    return all_user
