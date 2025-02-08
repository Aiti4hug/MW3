from django_filters import FilterSet
from .models import *

class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt']
        }