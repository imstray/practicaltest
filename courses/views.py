from django.shortcuts import render
from django.http import HttpResponse

from courses.models import CourseType
import templates

def index(request):
    return HttpResponse("MY app")

def course(request):
    courseList = CourseType.objects.all()
    contextDict = {}
    contextDict['courses'] = courseList
    return render(request, 'courses/course.html', context=contextDict)

# Create your views here.
