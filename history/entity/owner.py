from history.util.model_utils import randomId
from django.db.models import *
from history.entity.country import Country

class Owner(Model):
    street = CharField(max_length=128, help_text='street address')
    city = CharField(max_length=64)
    province_state = CharField(max_length=64, help_text='province/state/region')
    country = CharField(max_length=32, default=Country.CAN)
    phone_area_code = CharField(max_length=3)
    phone_number = CharField(max_length=7)
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=randomId())

    class Meta:
        abstract = True

class OwnerPerson(Owner):
    owner_person_id = CharField(max_length=128, primary_key=True, default=randomId())
    last_name = CharField(max_length=32)
    first_name = CharField(max_length=64)

class OwnerOrganization(Owner):
    owner_organization_id = CharField(max_length=128, primary_key=True, default=randomId())
    name = CharField(max_length=128)
    url = URLField(default='')

# captures inventory item's history of ownership
class InventoryOwnership(Model):
    inventory_ownership_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = ForeignKey('InventoryItem', on_delete=SET_NULL, null=True)
    owner_person_id = ForeignKey('OwnerPerson', on_delete=SET_NULL, null=True)
    owner_organization_id = ForeignKey('OwnerOrganization', on_delete=SET_NULL, null=True)
    user_key_create = CharField(max_length=128, default=None)
    created_at = DateTimeField(auto_now=True)
    ownership_start = DateTimeField()
    ownership_finish = DateTimeField()

