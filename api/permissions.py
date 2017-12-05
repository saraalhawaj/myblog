from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
	message = "Haaahaaa you don't have access."
	def has_object_permission(self, request, view, obj):
		if (request.user == obj.author) or (request.user.is_staff):
			return True
		else:
			return False


class IsOwner(BasePermission):
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff or (obj.author == request.user):
            return True
        else:
            return False