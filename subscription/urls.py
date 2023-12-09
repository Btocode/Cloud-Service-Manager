# subscription/urls.py

from django.urls import path
from .views import (
    SubscriptionPlanListCreateView, SubscriptionPlanDetailView,
    UserSubscriptionListCreateView, UserSubscriptionDetailView,
    PermissionListCreateView, PermissionDetailView, CheckUserPermissions
)

urlpatterns = [
    # Get all plans and create a new plan
    path('subscriptions/plans/', SubscriptionPlanListCreateView.as_view(), name='subscription-plan'),
    # Get a particular plan details, update a plan and delete a plan
    path('subscriptions/plans/<int:pk>/', SubscriptionPlanDetailView.as_view(), name='subscription-plan-op'),

    # Get all subscriptions and create a new subscription
    path('subscriptions/', UserSubscriptionListCreateView.as_view(), name='user-subscription-list'),
    # Get a particular subscription details, update a subscription and delete a subscription
    path('subscriptions/<int:pk>/', UserSubscriptionDetailView.as_view(), name='user-subscription-detail'),

    # Get all permissions and create a new permission
    path('permissions/', PermissionListCreateView.as_view(), name='permission-list'),
    # Get a particular permission details, update a permission and delete a permission
    path('permissions/<int:pk>/', PermissionDetailView.as_view(), name='permission-detail'),
    # Get usage stats on a subscription
    # path('subscriptions/<int:pk>/usage', GetUsageStatsOnSubscription.as_view(), name='subscription-usage'),
    # Check access permissions of a user
    path('access/<int:userId>/<int:pid>', CheckUserPermissions.as_view(), name='check-permissions'),
]
