# subscription/permissions.py

from rest_framework import permissions
from subscription.models import UserSubscription

class CustomAPIPermission(permissions.BasePermission):
    """
    Custom permission to check user access, update usage count, and block access if usage limit is exceeded.
    """

    def has_permission(self, request, view):
        user = request.user
        if user.is_admin:
            return True
        try:
            user_subscription = UserSubscription.objects.get(user=user)
        except UserSubscription.DoesNotExist:
            return False
        permissions = user_subscription.plan.permissions.all()

        # Check if the user has the required permission for the API endpoint
        api_endpoint = view.get_api_endpoint(request)

        for permission in permissions:
            if permission.api_endpoint == api_endpoint:
                # Update the usage count for the user subscription
                user_subscription.current_usage += 1
                
                # Check if current usage exceeds the usage limit
                if user_subscription.plan.usage_limit + user_subscription.custom_usage_limit < user_subscription.current_usage:
                    return False

                user_subscription.save()
                print("Permission granted")

                return True
        return False
