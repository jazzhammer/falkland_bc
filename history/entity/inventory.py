from history.util.model_utils import randomId
from django.db.models import *

class InventoryItem(Model):
    '''
                      __    _____
     _    _____  ____/ /__ / _/ /__ _    __
    | |/|/ / _ \/ __/  '_// _/ / _ \ |/|/ /
    |__,__/\___/_/ /_/\_\/_//_/\___/__,__/

    '''
    # identification workflow
    # just the id is required for creation
    # because the process of fully describing an inventory item is
    # disjoint, could take far more time than what would be required to fill out even a long form
    inventory_item_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_status_id = ForeignKey('InventoryStatus', on_delete=SET_NULL, null=True)

    # commonly referred to as when the item was entered into the database
    created_at = DateTimeField(auto_now=True)
    user_key_create = CharField(max_length=128, default='')

    # item physically received
    date_received = DateTimeField(auto_now=False, null=True)

    # when isbn is involved, when the isbn was issued
    date_registered = DateTimeField(auto_now=False, null=True)

    # entered into database.  different from the timestamp of the database record created
    date_entered = DateTimeField(auto_now=False, null=True)

    disposal_terms = TextField(help_text='', default='')

    '''
                                   __   __                  
      ___ ___  __ _____________  _/_/__/ /__  ___  ___  ____
     (_-</ _ \/ // / __/ __/ -_)/_// _  / _ \/ _ \/ _ \/ __/
    /___/\___/\_,_/_/  \__/\__/_/  \_,_/\___/_//_/\___/_/   
                                                            
    '''
    address_community = TextField(help_text='', default='')
    # donation workflow
    # all about the donor
    donor_person_id = ForeignKey('DonorPerson', on_delete=SET_NULL, null=True)
    donor_organization_id = ForeignKey('DonorOrganization', on_delete=SET_NULL, null=True)
    # item delivered by the donor
    donated_at = DateTimeField(auto_now=False, null=True)
    '''
         __                _      __  _         
     ___/ /__ ___ ________(_)__  / /_(_)__  ___ 
    / _  / -_|_-</ __/ __/ / _ \/ __/ / _ \/ _ \
    \_,_/\__/___/\__/_/ /_/ .__/\__/_/\___/_//_/ AND IDENTIFICATION
                         /_/                    
    '''
    # description workflow
    title = CharField(max_length=255, help_text='unique name, for conversational reference', default='')
    description = TextField(help_text='a paragraph, eg. that would tell someone something interesting about the item', default='')
    part_of = TextField(help_text='', default='')
    description_level = TextField(help_text='', default='')
    biography = TextField(help_text='', default='')
    url = URLField(null=True, help_text='if such exists, a url that we link to that provides more detail about the item', default='')

    # accession workflow
    # is there a document that comes along with getting an accession id ?
    # it could be an isbn, but not always
    accession_id = CharField(max_length=32, help_text='unique identifier, eg. ISBN', default='')
    notes = TextField(help_text='', default='')
    scope_and_content = TextField(help_text='', default='')
    related_material = TextField(help_text='', default='')
    #access:
    name_access = TextField(help_text='', default='')
    subject_access = TextField(help_text='', default='')
    '''
                           __         _                
      _ __  __ _ _ _ _  _ / _|__ _ __| |_ _  _ _ _ ___ 
     | '  \/ _` | ' \ || |  _/ _` / _|  _| || | '_/ -_)
     |_|_|_\__,_|_||_\_,_|_| \__,_\__|\__|\_,_|_| \___|
                                                       
    '''
    # general material designation + manufacture
    gmd = TextField(help_text='', default='')
    gmd_start = DateTimeField(auto_now=False, null=True)
    gmd_end = DateTimeField(auto_now=False, null=True)

    # manufacture
    date_range_start = DateTimeField(auto_now=False, null=True)
    date_range_end = DateTimeField(auto_now=False, null=True)
    # when an accession number was assigned, eg. isbn from the isbn agency, if it didn't already have one
    registered_at = DateTimeField(auto_now=False, null=True)
    manufacturer = TextField(help_text='', default='unknown')
    manufactured_from = DateTimeField(auto_now=False, null=True)
    manufactured_through = DateTimeField(auto_now=False, null=True)
    manufactured_in = CharField(max_length=128, help_text='', default='')
    manufacture_technique = CharField(max_length=128, help_text='', default='')

    # physical
    physical_description = TextField(help_text='', default='')
    physical_condition = TextField(help_text='', default='')
    inscription = CharField(max_length=128, help_text='', default='')
    length = IntegerField(default=0)
    width = IntegerField(default=0)
    height = IntegerField(default=0)



    '''
      _              _   
     | |__  ___  ___| |__
     | '_ \/ _ \/ _ \ / /
     |_.__/\___/\___/_\_\
                         
    '''

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
