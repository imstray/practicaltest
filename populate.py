import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GAapp.settings')

import django
django.setup()
from courses.models import CourseType

def populate():
    courseDescriptions = {'WES': 'This is the useful, most valuable and most inspiring course ever!',
                          'SE': 'This course is about good software engineering practices.'}

    startDates = {'WES': 'April 1, 2022',
                  'SE': 'June 1, 2022'}
    theCourses = {'Web Application Systems': {'Start Date': startDates['WES'], 'Description': courseDescriptions['WES']},
                      'Software Engineering': {'Start Date': startDates['SE'], 'Description': courseDescriptions['SE']}}


    for course, courseData in theCourses.items():
        c = add_course(course, courseData['Start Date'], courseData['Description'])

    for c in CourseType.objects.all():
        print(c)
def add_course(name, startDate, description):
    c = CourseType.objects.get_or_create(name=name)[0]
    c.startDate = startDate
    c.description = description
    c.save()
    return c

if __name__ == '__main__':
    print("Starting courses population script...")
    populate()