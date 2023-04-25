from history.util.model_utils import randomId
from django.db.models import *
from history.entity.country import Country

class InventoryItem(Model):
    # identification workflow
    inventory_item_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_status_id = ForeignKey('InventoryStatus', on_delete=SET_NULL, null=True)
    inventory_category_id = ForeignKey('InventoryCategory', on_delete=SET_NULL, null=True)

    # description workflow
    name = CharField(max_length=255, unique=True, help_text='unique name, for conversational reference')
    description = TextField(help_text='a paragraph, eg. that would tell someone something interesting about the item')
    biography = TextField(help_text='')
    url = URLField(null=True, help_text='if such exists, a url that we link to that provides more detail about the item')

    # accession workflow
    # is there a document that comes along with getting an accession id ?
    accession_id = CharField(max_length=32, unique=True, help_text='unique identifier, eg. ISBN')

    # donation workflow
    # all about the donor
    donor_person_id = ForeignKey('DonorPerson', on_delete=SET_NULL, null=True)
    donor_organization_id = ForeignKey('DonorOrganization', on_delete=SET_NULL, null=True)
    # item delivered by the donor
    donated_at = DateTimeField(auto_now=False, null=True)

    # physical description
    manufactured_from = DateTimeField(auto_now=False, null=True)
    manufactured_through = DateTimeField(auto_now=False, null=True)
    manufactured_in = CharField(max_length=128, help_text='')
    length = IntegerField()
    width = IntegerField()
    height = IntegerField()

    # when an accession number was assigned, eg. isbn from the isbn agency, if it didn't already have one
    registered_at = DateTimeField(auto_now=False, null=True)

    # commonly referred to as when the item was entered into the database
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=None)



class InventoryImage(Model):
    inventory_image_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = ForeignKey('InventoryItem', on_delete=SET_NULL, null=True)
    user_key_create = CharField(max_length=128, default=None)
    created_at = DateTimeField(auto_now=True)
    image = ImageField(upload_to='images/inventory', default=None)


class InventoryCategory(Model):
    inventory_category_id = CharField(max_length=128, primary_key=True, default=randomId())
    name = CharField(max_length=128, null=False)
    user_key_create = CharField(max_length=128, default=None)
    created_at = DateTimeField(auto_now=True)
    image = ImageField(upload_to='images/inventory', default=None)

