# auth/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer

from .models import CustomUser

class GetAllUsers(APIView):
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class AssignAdminApiView(APIView):
    def post(self, request, format=None):
        if 'id' not in request.data:
            return Response({
                'error': 'id is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = CustomUser.objects.get(id=request.data['id'])
            user.is_admin = True
            user.save()
            return Response({
                'message': 'Admin assigned successfully'
            },status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({
                'error': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)