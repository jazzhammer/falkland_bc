from history.util.model_utils import randomId
from django.db.models import *
from enum import Enum

class StatusName(Enum):
    # donor has delivered, awaiting accession
    NEW = 1,
    # has been assigned accession id, eg. isbn
    ACCESSIONED = 2,
    # ie. available for use/viewing
    AVAILABLE = 3,
    # ie. not available for use/viewing
    UNAVAILABLE = 4,
    # ie. will no longer be available for user/viewing
    RETIRED = 5

class InventoryStatus(Model):
    inventory_status_id = CharField(max_length=128, primary_key=True, default=randomId())
    name = CharField(max_length=128, default=StatusName.NEW)
    description = TextField(default=None)
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=None)

class InventoryStatusAssign(Model):
    inventory_status_assign_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = ForeignKey('InventoryItem', on_delete=SET_NULL, null=True)
    inventory_status_id = ForeignKey('InventoryStatus', to_field='inventory_status_id', on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=None)

