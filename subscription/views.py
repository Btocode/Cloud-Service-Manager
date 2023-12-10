# subscription/views.py

from rest_framework import generics
from .models import SubscriptionPlan, Permission, UserSubscription
from .serializers import SubscriptionPlanSerializer, PermissionSerializer, UserSubscriptionSerializer, SubscriptionPlanDetailSerializer, UserSubscriptionDetailsSerializer
from .permissions import IsAdminUserOrReadOnly, IsAdmin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class APiHealhCheckView(APIView):
    def get(self, request):
        return Response({
            "API Health Check": "Passed"
        },status=200)

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

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSubscriptionDetailsSerializer
        return UserSubscriptionSerializer


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


class ViewCurrentPlan(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionPlanSerializer

    def get(self, request):
        try:
            user_sub = UserSubscription.objects.get(user=request.user)
            serializer = SubscriptionPlanDetailSerializer(user_sub.plan)

            return Response(serializer.data)
        except UserSubscription.DoesNotExist:
            return Response({'error': 'You are not subscribe to any plans.'}, status=404)

class ViewUserStats(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_sub = UserSubscription.objects.get(user=request.user)
        except UserSubscription.DoesNotExist:
            return Response({'error': 'You are not subscribe to any plans.'}, status=404)

        serializer = UserSubscriptionDetailsSerializer(user_sub)
        usage_limit = user_sub.plan.usage_limit
        custom_usage_limit = user_sub.custom_usage_limit
        current_usage = user_sub.current_usage
        request_left = (usage_limit + custom_usage_limit) - current_usage
        if request_left < 0:
            request_left = 0
        return Response({
            'usage_limit': usage_limit,
            'custom_usage_limit': custom_usage_limit,
            'current_usage': current_usage,
            'request_left': request_left
        }, status=200)
        

class SubscribeToAPlan(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        plan_id = request.data.get('plan_id', None)
        
        if plan_id is None:
            return Response({'error': 'Plan ID is required.'}, status=400)
        
        try:
            plan = SubscriptionPlan.objects.get(id=plan_id)
        except SubscriptionPlan.DoesNotExist:
            return Response({'error': 'Plan not found.'}, status=404)
        
        try:
            user_sub = UserSubscription.objects.get(user=request.user)
        except UserSubscription.DoesNotExist:
            user_sub = UserSubscription(user=request.user, plan=plan)
        else:
            if user_sub.plan.id != plan.id:
                user_sub.plan = plan

        user_sub.save()

        return Response({'message': 'Plan subscribed successfully.'}, status=200)