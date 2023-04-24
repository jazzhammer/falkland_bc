from rest_framework import serializers
from .models import *


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = (
            'inventory_item_id',
            'name',
            'description',
            'url',
            'inventory_status_id',
            'user_key_create',
            'created_at',
        )


class InventoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryImage
        fields = (
            'inventory_image_id',
            'inventory_item_id',
            'user_key_create',
            'created_at',
            'image',
        )


class InventoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryStatus
        fields = (
            'inventory_status_id',
            'name',
            'description',
            'created_at',
            'user_key_create',
        )


class InventoryStatusAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryStatusAssign
        fields = (
            'inventory_status_assign_id',
            'inventory_item_id',
            'inventory_status_id',
            'created_at',
            'user_key_create',
        )


class InventoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLocation
        fields = (
            'inventory_location_id',
            'name',
            'description',
            'created_at',
            'user_key_create',
        )


class InventoryLocationAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLocationAssign
        fields = (
            'inventory_location_assign_id',
            'inventory_item_id',
            'inventory_location_id',
            'created_at',
            'user_key_create',
        )


class DonorPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorPerson
        fields = (
            'donor_person_id',
            'street',
            'city',
            'province_state',
            'country',
            'phone_area_code',
            'phone_number',
            'last_name',
            'first_name',
            'created_at',
            'user_key_create'
        )


class CreateDonorPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorPerson
        fields = [
            'street',
            'city',
            'province_state',
            'country',
            'phone_area_code',
            'phone_number',
            'last_name',
            'first_name'
        ]