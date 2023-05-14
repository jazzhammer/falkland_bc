from history.util.model_utils import randomId
from django.db.models import *

class InventoryItem(Model):
    # identification workflow
    inventory_item_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_status_id = ForeignKey('InventoryStatus', on_delete=SET_NULL, null=True)
    # inventory_category_id = ForeignKey('InventoryCategory', on_delete=SET_NULL, null=True)

    # item physically received
    date_received = DateTimeField(auto_now=False, null=True)

    # when isbn is involved, when the isbn was issued
    date_registered = DateTimeField(auto_now=False, null=True)

    # entered into database.  different from the timestamp of the database record created
    date_entered = DateTimeField(auto_now=False, null=True)
    address_community = TextField(help_text='', default='')

    # description workflow
    title = CharField(max_length=255, help_text='unique name, for conversational reference', default='')
    description = TextField(help_text='a paragraph, eg. that would tell someone something interesting about the item', default='')
    part_of = TextField(help_text='', default='')
    disposal_terms = TextField(help_text='', default='')
    description_level = TextField(help_text='', default='')
    biography = TextField(help_text='', default='')
    url = URLField(null=True, help_text='if such exists, a url that we link to that provides more detail about the item', default='')

    # accession workflow
    # is there a document that comes along with getting an accession id ?
    # it could be an isbn, but not always
    accession_id = CharField(max_length=32, unique=True, help_text='unique identifier, eg. ISBN')

    # general material designation
    gmd_options = (
        'architectural drawing',
        'cartographic material',
        'graphic material',
        'moving images',
        'multiple media',
        'object',
        'philatelic record',
        'sound recording',
        'technical drawing',
        'textual record',
        'electronic',
        'large print',
        'microform',
        'tactile'
    )
    gmd = TextField(help_text='', default='')
    gmd_start = DateTimeField(auto_now=False, null=True)
    gmd_end = DateTimeField(auto_now=False, null=True)
    date_range_start = DateTimeField(auto_now=False, null=True)
    date_range_end = DateTimeField(auto_now=False, null=True)
    # when an accession number was assigned, eg. isbn from the isbn agency, if it didn't already have one
    registered_at = DateTimeField(auto_now=False, null=True)


    # donation workflow
    # all about the donor
    donor_person_id = ForeignKey('DonorPerson', on_delete=SET_NULL, null=True)
    donor_organization_id = ForeignKey('DonorOrganization', on_delete=SET_NULL, null=True)
    # item delivered by the donor
    donated_at = DateTimeField(auto_now=False, null=True)

    # physical description
    physical_description = TextField(help_text='', default='')
    physical_condition = TextField(help_text='', default='')
    manufacturer = TextField(help_text='', default='unknown')
    manufactured_from = DateTimeField(auto_now=False, null=True)
    manufactured_through = DateTimeField(auto_now=False, null=True)
    manufactured_in = CharField(max_length=128, help_text='')
    manufacture_technique = CharField(max_length=128, help_text='', default='')
    inscription = CharField(max_length=128, help_text='', default='')
    length = IntegerField()
    width = IntegerField()
    height = IntegerField()
    notes = TextField(help_text='', default='')
    scope_and_content = TextField(help_text='', default='')
    related_material = TextField(help_text='', default='')

    #access:
    name_access = TextField(help_text='', default='')
    subject_access = TextField(help_text='', default='')

    # commonly referred to as when the item was entered into the database
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default=None)

    # when the item is a book:
    title_page_title = TextField(help_text='', default='')
    spine_title = TextField(help_text='', default='')
    # use manufactured_in for publication_place
    # use manufacturer for publisher
    # use manufactured_from for published ymd
    edition = TextField(help_text='', default='')
    numbered_pages = IntegerField(default=0)
    is_hardcover = BooleanField(default=True)
    cover_color = TextField(help_text='', default='')
    # this one looks suspicious, asked denise
    record_type = TextField(help_text='', default='')
    subject_names = TextField(help_text='', default='')
    summary = TextField(help_text='', default='')
