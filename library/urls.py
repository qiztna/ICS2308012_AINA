from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.view, name="view"),
    path("database/", views.database, name="database"),
    path("course/", views.course, name="course"),
    path("mentor/", views.newmentor, name="newmentor"),
    path("course/search/", views.search_course, name="search_course"),
    path("mentor/search/", views.search_mentor, name="search_mentor"),
    path("course/update_course/<str:code>", views.update_course, name="update_course"),
    path("mentor/update_mentor/<str:mentorID>", views.update_mentor, name="update_mentor"),
    path("course/update_course/save_update_course/<str:code>", views.save_update_course, name="save_update_course"),
    path("mentor/update_mentor/save_update_mentor/<str:mentorID>", views.save_update_mentor, name="save_update_mentor"),
    path("course/delete_course/<str:code>", views.delete_course, name="delete_course"),
    path("mentor/delete_mentor/<str:mentorID>", views.delete_mentor, name="delete_mentor"),
]