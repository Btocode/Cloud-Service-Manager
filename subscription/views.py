# subscription/views.py

from rest_framework import generics
from .models import SubscriptionPlan, Permission, UserSubscription
from .serializers import SubscriptionPlanSerializer, PermissionSerializer, UserSubscriptionSerializer, SubscriptionPlanDetailSerializer
from .permissions import IsAdminUserOrReadOnly

class SubscriptionPlanListCreateView(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubscriptionPlanDetailSerializer
        return SubscriptionPlanSerializer 


class SubscriptionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    # if get request, use SubscriptionPlanDetailSerializer
    # if post request, use SubscriptionPlanSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubscriptionPlanDetailSerializer
        return SubscriptionPlanSerializer 

class UserSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UserSubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PermissionListCreateView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class PermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUserOrReadOnly]

