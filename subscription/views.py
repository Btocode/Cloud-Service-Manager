# subscription/views.py

from rest_framework import generics
from .models import SubscriptionPlan, Permission, UserSubscription
from .serializers import SubscriptionPlanSerializer, PermissionSerializer, UserSubscriptionSerializer, SubscriptionPlanDetailSerializer, UserSubscriptionDetailsSerializer
from .permissions import IsAdminUserOrReadOnly, IsAdmin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class SubscriptionPlanListCreateView(generics.ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubscriptionPlanDetailSerializer
        return SubscriptionPlanSerializer 


class SubscriptionPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    # if get request, use SubscriptionPlanDetailSerializer
    # if post request, use SubscriptionPlanSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubscriptionPlanDetailSerializer
        return SubscriptionPlanSerializer 

class UserSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]


class UserSubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSubscriptionDetailsSerializer
        return UserSubscriptionSerializer

class PermissionListCreateView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]


class PermissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]


class CheckUserPermissions(APIView):
    permission_classes = [IsAdmin]

    def get(self, request, userId, pid):
        try:
            user_sub = UserSubscription.objects.get(user__id=userId)
        except UserSubscription.DoesNotExist:
            return Response({'access': 'Declined'}, status=404)
        except SubscriptionPlan.DoesNotExist:
            return Response({'access': 'Declined'}, status=404)

        for permission in user_sub.plan.permissions.all():
            if permission.id == pid:
                if user_sub.plan.usage_limit + user_sub.custom_usage_limit < user_sub.current_usage:
                    return Response({'access': 'Blocked'}, status=200)
                return Response({'access': 'Granted'}, status=200)
        
        return Response({'access': 'Declined'}, status=403)

