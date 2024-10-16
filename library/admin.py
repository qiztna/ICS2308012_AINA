from django.contrib import admin

# Register your models here.
from library.models import Course, Student, Mentor
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Mentor)

