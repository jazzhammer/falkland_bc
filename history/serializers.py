from rest_framework import serializers

from history.entity.donor import DonorPerson
from history.entity.inventory import InventoryItem
from history.entity.inventory_location import InventoryLocation, InventoryLocationAssign
from history.entity.inventory_status import InventoryStatus, InventoryStatusAssign
import history.serialize.donor
import history.serialize.inventory_location
import history.serialize.inventory_status

from .entity.product import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
