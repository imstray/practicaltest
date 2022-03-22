from django.db import models

# Create your models here.

class CourseType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    startDate = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name