from rest_framework import permissions

METHODS_FOR_ANON_USER = ('GET', )
METHODS_FOR_AUTH_USER = ('POST', )
METHODS_FOR_AUTHOR = ('PATCH', 'PUT', 'DELETE')


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in METHODS_FOR_AUTHOR:
            return obj.author == request.user
        if request.method in METHODS_FOR_AUTH_USER:
            return request.user.is_authenticated
        if request.method in METHODS_FOR_ANON_USER:
            return True
        return False
