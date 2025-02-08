from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Network)
class NetworkTranslationOptions(TranslationOptions):
    fields = ('network_name', 'title')


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)