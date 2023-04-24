from django.db import models
from enum import Enum

import secrets
import string

def randomId():
    alphabet = string.ascii_letters + string.digits
    id = ''.join(secrets.choice(alphabet) for i in range(126))
    print(f'id({len(id)}): {id}')
    return id


class InventoryItem(models.Model):
    inventory_item_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    name = models.CharField(max_length=255, unique=True, help_text='unique name, for conversational reference')
    description = models.TextField(help_text='a paragraph, eg. that would tell someone something interesting about the item')
    url = models.URLField(null=True, help_text='if such exists, a url that we link to that provides more detail about the item')
    inventory_status_id = models.ForeignKey('InventoryStatus', on_delete=models.SET_NULL, null=True)
    user_key_create = models.CharField(max_length=128, default=None)
    donated_at = models.DateTimeField(auto_now=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    donor_person_id = models.ForeignKey('DonorPerson', on_delete=models.SET_NULL, null=True)
    donor_organization_id = models.ForeignKey('DonorOrganization', on_delete=models.SET_NULL, null=True)

class InventoryImage(models.Model):
    inventory_image_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = models.ForeignKey('InventoryItem', on_delete=models.SET_NULL, null=True)
    user_key_create = models.CharField(max_length=128, default=None)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/inventory', default=None)

class StatusName(Enum):
    NEW = 1,
    VALID = 2,
    AVAILABLE = 3,
    UNAVAILABLE = 4,
    RETIRED = 5

class InventoryStatus(models.Model):
    inventory_status_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    name = models.CharField(max_length=128, default=StatusName.NEW)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now=True)
    user_key_create = models.CharField(max_length=128, default=None)

class InventoryStatusAssign(models.Model):
    inventory_status_assign_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = models.ForeignKey('InventoryItem', on_delete=models.SET_NULL, null=True)
    inventory_status_id = models.ForeignKey('InventoryStatus', to_field='inventory_status_id', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    user_key_create = models.CharField(max_length=128, default=None)

class InventoryLocation(models.Model):
    inventory_location_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    name = models.CharField(max_length=128)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now=True)
    user_key_create = models.CharField(max_length=128, default=None)

class InventoryLocationAssign(models.Model):
    inventory_location_assign_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = models.ForeignKey('InventoryItem', on_delete=models.SET_NULL, null=True)
    inventory_location_id = models.ForeignKey('InventoryLocation', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    user_key_create = models.CharField(max_length=128, default=None)


class Country(Enum):
    CAN = 1
    USA = 2
    UK = 3

class Donor(models.Model):
    street = models.CharField(max_length=128, help_text='street address')
    city = models.CharField(max_length=64)
    province_state = models.CharField(max_length=64, help_text='province/state/region')
    country = models.CharField(max_length=32, default=Country.CAN)
    phone_area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now=True)
    user_key_create = models.CharField(max_length=128, default=randomId())

    class Meta:
        abstract = True

class DonorPerson(Donor):
    donor_person_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    last_name = models.CharField(max_length=32)
    first_name = models.CharField(max_length=64)

class DonorOrganization(Donor):
    donor_organization_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    name = models.CharField(max_length=128)
    url = models.URLField(default='')
