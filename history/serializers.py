from rest_framework import serializers

from history.entity.donor import DonorPerson
from history.entity.inventory import InventoryItem, InventoryImage
from history.entity.inventory_location import InventoryLocation, InventoryLocationAssign
from history.entity.inventory_status import InventoryStatus, InventoryStatusAssign
import history.serialize.donor
import history.serialize.inventory_location
import history.serialize.inventory_status

