from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from rest_framework.exceptions import ValidationError

ROLE_CHOICES = (
    ('teacher', 'teacher'),
    ('student', 'student'),
)

STATUS_CHOICES = (
        ('ez', 'ez'),
        ('norm', 'norm'),
        ('hard', 'hard')
    )


class Profile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    age = models.PositiveSmallIntegerField(verbose_name='age', null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(80)])
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Network(models.Model):
    network_name = models.CharField(max_length=32)
    network_link = models.URLField()
    title = models.CharField(max_length=64, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, {self.network_name}'

class Teacher(Profile):
    bio = models.TextField()
    DAYS_CHOiCES = (
        ('Mo', 'Mo'),
        ('Tu', 'Tu'),
        ('We', 'We'),
        ('Th', 'Th'),
        ('Fr', 'Fr'),
        ('Sa', 'Sa'),
        ('Su', 'Su')
    )
    work_days = MultiSelectField(max_length=16, choices=DAYS_CHOiCES, max_choices=6)
    subject = models.TextField()
    experience = models.PositiveSmallIntegerField(validators=[MinValueValidator(21), MaxValueValidator(45)])
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='teacher')

    def __str__(self):
        return f'{self.first_name}, {self.role}'

    class Meta:
        verbose_name_plural = 'teachers'

class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f'{self.user}, {self.role}'

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name

class Course(models.Model):
    course_name = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ManyToManyField(Teacher)
    level = models.CharField(max_length=32, choices=STATUS_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    TYPE_CHOICES = (
        ('free', 'free'),
        ('paid', 'paid')
    )
    type_course = models.CharField(max_length=32, choices=TYPE_CHOICES)
    created_ap = models.DateTimeField(auto_now_add=True)
    updated_ap = models.DateTimeField(auto_now=True)
    course_certificate = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    title = models.CharField(max_length=32)
    video_url = models.URLField(null=True, blank=True)
    video = models.FileField(upload_to='course_video', null=True, blank=True)
    content = models.FileField(upload_to='course_document', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course}, {self.title}'

class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Exam(models.Model):
    title = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    end_time = models.DurationField

    def __str__(self):
        return f'{self.title}, {self.course}'

class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                         MaxValueValidator(100)])

    def __str__(self):
        return f'{self.exam}, {self.title}'

class Option(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    variant = models.CharField(max_length=64)
    option_check = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.variant}, {self.check}'

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(upload_to='certificate')

    def __str__(self):
        return f'{self.student}, {self.course}'

class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)],
                                             null=True, blank=True)

    def __str__(self):
        return f'{self.user}, {self.course}'

    def clean(self):
        super().clean()
        if not self.text and not self.stars:
            raise ValidationError('Choose minimum one of (text, stars)!')


class TeacherRating(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'{self.teacher}, {self.stars}'

class History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course

class Cart(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Favorite(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)