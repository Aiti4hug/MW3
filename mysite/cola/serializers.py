from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name',
                  'age','email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'profile_picture', 'age', 'phone_number']

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['network_name', 'title']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['work_days', 'experience']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseListSerializer(serializers.ModelSerializer):
    created_ap = serializers.DateTimeField(format('%m-%d-%Y'))
    updated_ap = serializers.DateTimeField(format('%m-%d-%Y'))

    class Meta:
        model = Course
        fields = ['course_name', 'category', 'author', 'level', 'price', 'created_ap', 'updated_ap']

class CourseDetailSerializer(serializers.ModelSerializer):
    created_ap = serializers.DateTimeField(format('%m-%d-%Y'))
    updated_ap = serializers.DateTimeField(format('%m-%d-%Y'))

    class Meta:
        model = Course
        fields = ['course_name', 'category', 'author', 'level', 'price', 'created_ap', 'updated_ap']


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'author', 'level', 'price', 'type_course']

class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'author', 'level', 'price', 'type_course']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField(format('%m-%d-%Y'))

    class Meta:
        model = Assignment
        fields = ['title', 'course', 'due_date']

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'

class TeacherRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherRating
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'
