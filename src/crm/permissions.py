from rest_framework.permissions import BasePermission


class IsSale(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'sale'


class IsSupport(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'support'


class IsManagement(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'management'
