# cloud_services/api/models.py
from django.db import models

class CloudService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# cloud_services/api/models/cloud_storage.py
class CloudStorage(models.Model):
    name = models.CharField(max_length=255)
    capacity_gb = models.IntegerField()
    price_per_gb = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# cloud_services/api/models/cloud_compute.py
class CloudCompute(models.Model):
    name = models.CharField(max_length=255)
    cpu_cores = models.IntegerField()
    ram_gb = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# cloud_services/api/models/cloud_database.py
class CloudDatabase(models.Model):
    name = models.CharField(max_length=255)
    db_engine = models.CharField(max_length=255)
    storage_gb = models.IntegerField()
    price_per_gb = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# cloud_services/api/models/cloud_analytics.py
class CloudAnalytics(models.Model):
    name = models.CharField(max_length=255)
    analytics_type = models.CharField(max_length=255)
    price_per_query = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# cloud_services/api/models/cloud_networking.py
class CloudNetworking(models.Model):
    name = models.CharField(max_length=255)
    bandwidth_gbps = models.FloatField()
    price_per_gb = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# cloud_services/api/models/cloud_security.py
class CloudSecurity(models.Model):
    name = models.CharField(max_length=255)
    security_type = models.CharField(max_length=255)
    price_per_month = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
