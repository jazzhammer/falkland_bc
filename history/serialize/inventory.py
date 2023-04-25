from rest_framework.serializers import ModelSerializer
from history.entity.inventory import InventoryItem
from history.entity.inventory import InventoryImage

class InventoryItemSerializer(ModelSerializer):
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


class InventoryImageSerializer(ModelSerializer):
    class Meta:
        model = InventoryImage
        fields = (
            'inventory_image_id',
            'inventory_item_id',
            'user_key_create',
            'created_at',
            'image',
        )

