from history.util.model_utils import randomId
from django.db.models import *


class InventoryLocation(Model):
    inventory_location_id = CharField(max_length=128, primary_key=True, default=randomId())
    name = CharField(max_length=128)
    description = TextField(default=None)
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=None)

class InventoryLocationAssign(Model):
    inventory_location_assign_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = ForeignKey('InventoryItem', on_delete=SET_NULL, null=True)
    inventory_location_id = ForeignKey('InventoryLocation', on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=None)
