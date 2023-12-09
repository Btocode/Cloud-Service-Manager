# auth/views.py

from rest_framework import generics
from .models import SubscriptionPlan, Permission, UserSubscription
from .serializers import SubscriptionPlanSerializer, PermissionSerializer, UserSubscriptionSerializer

# # Get all plans and create a new plan
# path('subscriptions/plans/', SubscriptionPlanListCreateView.as_view(), name='subscription-plan'),

class SubscriptionPlanListCreateView(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)


class SubscriptionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer

class PermissionListCreateView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

class UserSubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
