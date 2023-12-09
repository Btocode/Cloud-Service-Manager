# cloud_services/api/views.py
from rest_framework import viewsets
from .models import CloudService, CloudStorage, CloudCompute, CloudDatabase, CloudAnalytics, CloudNetworking, CloudSecurity
from .serializers import (
    CloudServiceSerializer, CloudStorageSerializer, CloudComputeSerializer,
    CloudDatabaseSerializer, CloudAnalyticsSerializer, CloudNetworkingSerializer, CloudSecuritySerializer
)

class CloudServiceViewSet(viewsets.ModelViewSet):
    queryset = CloudService.objects.all()
    serializer_class = CloudServiceSerializer

class CloudStorageViewSet(viewsets.ModelViewSet):
    queryset = CloudStorage.objects.all()
    serializer_class = CloudStorageSerializer

class CloudComputeViewSet(viewsets.ModelViewSet):
    queryset = CloudCompute.objects.all()
    serializer_class = CloudComputeSerializer

class CloudDatabaseViewSet(viewsets.ModelViewSet):
    queryset = CloudDatabase.objects.all()
    serializer_class = CloudDatabaseSerializer

class CloudAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = CloudAnalytics.objects.all()
    serializer_class = CloudAnalyticsSerializer

class CloudNetworkingViewSet(viewsets.ModelViewSet):
    queryset = CloudNetworking.objects.all()
    serializer_class = CloudNetworkingSerializer

class CloudSecurityViewSet(viewsets.ModelViewSet):
    queryset = CloudSecurity.objects.all()
    serializer_class = CloudSecuritySerializer
