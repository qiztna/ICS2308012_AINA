from django.shortcuts import render
from library.models import Student,Book,Borrowing,Course,Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'greeting' : 1,
    }
    return render (request, "index.html", context)

def view(request):
    context = {
        'firstname' : 'Aryan',
    }
    return render (request, "view.html", context)

def database(request):
    data1 = Book.objects.all().values()
    data2 = Student.objects.all().values()
    data3 = Borrowing.objects.all().values()
    context = {
        'data1' : data1,
        'data2' : data2,
        'data3' : data3,
    }
    return render (request, "database.html", context)

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['description']
        data = Course(code=c_code, description=c_desc)
        data.save()
        mycourse = Course.objects.all().values()
        dict = {
            'message':'Data Save',
            'mycourse': mycourse,
        }
    else:
        dict = {
            'message':'',
        }
    return render (request, "course.html", dict)

def newmentor(request):
    if request.method == 'POST':
        men_id = request.POST['mentorID']
        men_name = request.POST['mentorName']
        men_room = request.POST['roomNo']
        data = Mentor(mentorID=men_id, mentorName=men_name, roomNo=men_room)
        data.save()
        mymentors = Mentor.objects.all().values()
        dict = {
            'message':'Data Save',
            'mymentors': mymentors,
        }
    else:
        dict = {
            'message':'',
        }
    return render (request, "newmentor.html", dict)



def update_course(request,code):
    data = Course.objects.get(code=code)
    dict = {
            'data':data,
        }
    return render (request, "update_course.html", dict)

def update_mentor(request,mentorID):
    data = Mentor.objects.get(mentorID=mentorID)
    dict = {
            'data':data,
        }
    return render (request, "update_mentor.html", dict)



def save_update_course(request,code):
    c_desc = request.POST['description']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def save_update_mentor(request,mentorID):
    men_name = request.POST['mentorName']
    men_room = request.POST['roomNo']
    data = Mentor.objects.get(mentorID=mentorID)
    data.mentorName = men_name
    data.roomNo = men_room
    data.save()
    return HttpResponseRedirect(reverse("newmentor"))



def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse("course"))

def delete_mentor(request, mentorID):
    data = Mentor.objects.get(mentorID=mentorID)
    data.delete()
    return HttpResponseRedirect(reverse("newmentor"))



# views
def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')
        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None
        context = {
            'data':data
        }
        return render(request, "search_course.html", context)
    return render(request, "search_course.html")


def search_mentor(request):
    if request.method == 'GET':
        men_id = request.GET.get('men_id')
        if men_id:
            data = Mentor.objects.filter(mentorID=men_id.upper())
        else:
            data = None
        context = {
            'data':data
        }
        return render(request, "search_mentor.html", context)
    return render(request, "search_mentor.html")