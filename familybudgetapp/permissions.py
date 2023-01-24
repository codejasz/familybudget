from rest_framework import permissions


class IsOwnerOrIsPermitted(permissions.BasePermission):
    """
    Object-level permission to only allow owners or users
    allowed by owner to view object.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if obj.shared_with.filter(shared_with_id=request.user.id).exists():
            return True
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
