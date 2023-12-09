# cloud_services/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CloudServiceViewSet, CloudStorageViewSet, CloudComputeViewSet,
    CloudDatabaseViewSet, CloudAnalyticsViewSet, CloudNetworkingViewSet, CloudSecurityViewSet
)

router = DefaultRouter()

router.register(r'cloud-services', CloudServiceViewSet)
router.register(r'cloud-storage', CloudStorageViewSet)
router.register(r'cloud-compute', CloudComputeViewSet)
router.register(r'cloud-database', CloudDatabaseViewSet)
router.register(r'cloud-analytics', CloudAnalyticsViewSet)
router.register(r'cloud-networking', CloudNetworkingViewSet)
router.register(r'cloud-security', CloudSecurityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
