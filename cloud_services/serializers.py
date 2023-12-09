# cloud_services/api/serializers.py
from rest_framework import serializers
from .models import CloudService, CloudStorage, CloudCompute, CloudDatabase, CloudAnalytics, CloudNetworking, CloudSecurity

class CloudServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudService
        fields = ('id', 'name', 'description')


# cloud_services/api/serializers/cloud_storage.py
class CloudStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudStorage
        fields = ('id', 'name', 'capacity_gb', 'price_per_gb')


# cloud_services/api/serializers/cloud_compute.py
class CloudComputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudCompute
        fields = ('id', 'name', 'cpu_cores', 'ram_gb', 'price_per_hour')


# cloud_services/api/serializers/cloud_database.py
class CloudDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudDatabase
        fields = ('id', 'name', 'db_engine', 'storage_gb', 'price_per_gb')


# cloud_services/api/serializers/cloud_analytics.py
class CloudAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudAnalytics
        fields = ('id', 'name', 'analytics_type', 'price_per_query')


# cloud_services/api/serializers/cloud_networking.py
class CloudNetworkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudNetworking
        fields = ('id', 'name', 'bandwidth_gbps', 'price_per_gb')


# cloud_services/api/serializers/cloud_security.py
class CloudSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudSecurity
        fields = ('id', 'name', 'security_type', 'price_per_month')
