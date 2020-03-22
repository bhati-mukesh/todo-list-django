from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    task = models.CharField(max_length=200,default='')
    publishedDate = models.DateField()
    priority = models.IntegerField(default=0)
    doneToBeDate = models.DateField()
    userId = models.IntegerField(default=0)
    complete = models.CharField(max_length=5,default='')

    def __str__(self):
        return self.task[:30]

# class CompletedTask(models.Model):
#     ctaskID = models.AutoField(primary_key=True)
#     taskID = models.IntegerField(default=0)
#     task = models.CharField(max_length=200,default='')
#     publishedDate = models.DateField()
#     userId = models.IntegerField(default=0)

#     def __str__(self):
#         return self.task[:30]
