from rest_framework.permissions import BasePermission


class IsAnonymous(BasePermission):
    """
    Allows access only to Anonymous people.
    """
    def has_permission(self, request, view):
        return bool(not request.user.is_authenticated)


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return(
            request.method in ('GET', 'HEAD', 'OPTIONS') or
            obj.username == request.user.username
        )
