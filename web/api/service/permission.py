from rest_framework import permissions

def isOwner(request, obj):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    if request.method in permissions.SAFE_METHODS:
        return True

    # Instance must have an attribute named `owner`.

    return (
        (request.user is not None) and
        (request.user.is_authenticated) and
        (request.user.id == obj.creator.user.id)
    )