# subscription/serializers.py

from rest_framework import serializers
from .models import SubscriptionPlan, Permission, UserSubscription

# subscription/serializers.py

from rest_framework import serializers
from .models import Permission, SubscriptionPlan

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'api_endpoint', 'description']

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    # get all the permissions from permission serializer
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'description', 'usage_limit', 'permissions']

    # Override create and update methods to handle ManyToManyField permissions
    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions', [])
        plan = SubscriptionPlan.objects.create(**validated_data)
        plan.permissions.set(permissions_data)
        return plan

    def update(self, instance, validated_data):
        permissions_data = validated_data.pop('permissions', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.usage_limit = validated_data.get('usage_limit', instance.usage_limit)
        instance.permissions.set(permissions_data)
        instance.save()
        return instance

class SubscriptionPlanDetailSerializer(serializers.ModelSerializer):
    # get all the permissions from permission serializer
    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'description', 'usage_limit', 'permissions']

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'
