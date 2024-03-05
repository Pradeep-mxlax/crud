from django.db import models


# Create your models here.
class Person(models.Model):
   username = models.CharField(max_length=30)
   password = models.CharField(max_length=30)

   def __str__(self):
      return self.username
   

# # myapp/models.py

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=50)

#    #  def __str__(self):
#    #     return self.author