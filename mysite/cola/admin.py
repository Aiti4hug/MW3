from django.contrib import admin
import nested_admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import (Profile, Network, Teacher, Student, Category, Course, Lesson, Assignment,
                     Exam, Questions, Option, Certificate, CourseReview, TeacherRating, History,
                     Cart, CartItem, Favorite, FavoriteItem)


class OptionInline(nested_admin.NestedStackedInline):
    model = Option
    extra = 1


class QuestionsInline(nested_admin.NestedStackedInline):
    model = Questions
    extra = 1
    inlines = [OptionInline]


@admin.register(Exam)
class ExamAdmin(TranslationAdmin, nested_admin.NestedModelAdmin):
    inlines = [QuestionsInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class CartItemInline(admin.TabularInline):
    model =CartItem
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


class FavoriteItemInline(admin.TabularInline):
    model = FavoriteItem
    extra = 1


class FavoriteAdmin(admin.ModelAdmin):
    inlines = [FavoriteItemInline]


class GeneralMedia:
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Network)
class NetworkAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Course)
class CourseAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Lesson)
class LessonAdmin(TranslationAdmin, GeneralMedia):
    pass


@admin.register(Assignment)
class AssignmentAdmin(TranslationAdmin, GeneralMedia):
    pass


# @admin.register(Exam)
# class ExamAdmin(TranslationAdmin, GeneralMedia):
#     inlines = [ExamAllAdmin]


admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Certificate)
# admin.site.register(Exam, ExamAllAdmin)
admin.site.register(CourseReview)
admin.site.register(TeacherRating)
admin.site.register(History)
admin.site.register(Cart, CartAdmin)
admin.site.register(Favorite, FavoriteAdmin)
