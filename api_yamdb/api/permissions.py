from rest_framework import permissions


class ReadOrAuthorAndStaff(permissions.BasePermission):
    """ Редактирование для автора, либо для стафа. """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and (
                obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator
            )
        )


class Admin(permissions.BasePermission):
    """ Пермишен для прав модератор и админ. """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )


class AdminOrReadOnly(permissions.BasePermission):
    """ Пермишен для прав модератор и админ. """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or (
                request.user.is_authenticated
                and request.user.is_admin
            )
        )
