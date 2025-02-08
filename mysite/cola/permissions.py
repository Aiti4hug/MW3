from rest_framework import permissions

class CheckStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'

class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and hasattr(request.user, 'teacher')

class IsExamOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.course.author.filter(id=request.user.id).exists()
