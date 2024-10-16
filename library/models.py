from django.db import models

# Create your models here.
class Book(models.Model):
    bookID = models.CharField(max_length=4, primary_key = True)
    title = models.TextField()
    author = models.TextField()
    year = models.CharField(max_length=4)

class Student(models.Model):
    id = models.CharField(max_length=12, primary_key = True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=150)
    status = models.CharField(max_length=10, default='Active')

class Borrowing(models.Model):
    borrowID = models.CharField(max_length=12, primary_key = True)
    bookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    id = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrowDate = models.DateField(max_length=100)
    returnDate = models.DateField(max_length=12)

class Course(models.Model):
    code = models.CharField(max_length=4, primary_key = True)
    description = models.TextField(max_length=100)

class Mentor(models.Model):
    mentorID = models.CharField(max_length=8, primary_key = True)
    mentorName = models.CharField(max_length=225)
    roomNo = models.CharField(max_length=3, default='sk2')




