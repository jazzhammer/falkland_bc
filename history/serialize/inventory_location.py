from rest_framework.serializers import ModelSerializer
from history.entity.inventory_location import InventoryLocation
from history.entity.inventory_location import InventoryLocationAssign


class InventoryLocationSerializer(ModelSerializer):
    class Meta:
        model = InventoryLocation
        fields = (
            'inventory_location_id',
            'name',
            'description',
            'created_at',
            'user_key_create',
        )


class InventoryLocationAssignSerializer(ModelSerializer):
    class Meta:
        model = InventoryLocationAssign
        fields = (
            'inventory_location_assign_id',
            'inventory_item_id',
            'inventory_location_id',
            'created_at',
            'user_key_create',
        )

