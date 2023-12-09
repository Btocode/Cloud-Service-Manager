# cloud_services/api/views.py
from rest_framework import viewsets
from .models import CloudService, CloudStorage, CloudCompute, CloudDatabase, CloudAnalytics, CloudNetworking, CloudSecurity
from .serializers import (
    CloudServiceSerializer, CloudStorageSerializer, CloudComputeSerializer,
    CloudDatabaseSerializer, CloudAnalyticsSerializer, CloudNetworkingSerializer, CloudSecuritySerializer
)
from .permissions import CustomAPIPermission
from rest_framework.permissions import IsAuthenticated

class CloudServiceViewSet(viewsets.ModelViewSet):
    queryset = CloudService.objects.all()
    serializer_class = CloudServiceSerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-services/'


class CloudStorageViewSet(viewsets.ModelViewSet):
    queryset = CloudStorage.objects.all()
    serializer_class = CloudStorageSerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-storage/'


class CloudComputeViewSet(viewsets.ModelViewSet):
    queryset = CloudCompute.objects.all()
    serializer_class = CloudComputeSerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-compute/'


class CloudDatabaseViewSet(viewsets.ModelViewSet):
    queryset = CloudDatabase.objects.all()
    serializer_class = CloudDatabaseSerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-database/'


class CloudAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = CloudAnalytics.objects.all()
    serializer_class = CloudAnalyticsSerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-analytics/'


class CloudNetworkingViewSet(viewsets.ModelViewSet):
    queryset = CloudNetworking.objects.all()
    serializer_class = CloudNetworkingSerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-networking/'


class CloudSecurityViewSet(viewsets.ModelViewSet):
    queryset = CloudSecurity.objects.all()
    serializer_class = CloudSecuritySerializer
    permission_classes = [IsAuthenticated, CustomAPIPermission]

    def get_api_endpoint(self, request):
        # Customize this method to extract the API endpoint from the request
        return '/services/cloud-security/'

