from rest_framework.serializers import ModelSerializer
from history.entity.inventory_status import InventoryStatus
from history.entity.inventory_status import InventoryStatusAssign

class InventoryStatusSerializer(ModelSerializer):
    class Meta:
        model = InventoryStatus
        fields = (
            'inventory_status_id',
            'name',
            'description',
            'created_at',
            'user_key_create',
        )


class InventoryStatusAssignSerializer(ModelSerializer):
    class Meta:
        model = InventoryStatusAssign
        fields = (
            'inventory_status_assign_id',
            'inventory_item_id',
            'inventory_status_id',
            'created_at',
            'user_key_create',
        )


