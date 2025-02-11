from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'course-reviews', CourseReviewViewSet)
router.register(r'teacher-ratings', TeacherRatingViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite-items', FavoriteItemViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('category/', CategoryAPIView.as_view(), name='categorys'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('courses/create/', CourseCreateAPIView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', CourseUpdateAPIView.as_view(), name='course-update'),
]