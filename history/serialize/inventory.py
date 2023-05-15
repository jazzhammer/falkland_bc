from rest_framework.serializers import ModelSerializer
from history.entity.inventory import InventoryItem
from history.entity.inventory_image import InventoryImage


class InventoryItemSerializer(ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = (
            'inventory_item_id',
            'inventory_status_id',
            'created_at',
            'user_key_create',
            'date_received',
            'date_registered',
            'date_entered',
            'disposal_terms',
            'address_community',
            'donor_person_id',
            'donor_organization_id',
            'donated_at',
            'title',
            'description',
            'part_of',
            'description_level',
            'biography',
            'url',
            'accession_id',
            'notes',
            'scope_and_content',
            'related_material',
            'name_access',
            'subject_access',
            'gmd',
            'gmd_start',
            'gmd_end',
            'date_range_start',
            'date_range_end',
            'registered_at',
            'manufacturer',
            'manufactured_from',
            'manufactured_through',
            'manufactured_in',
            'manufacture_technique',
            'physical_description',
            'physical_condition',
            'inscription',
            'length',
            'width',
            'height',
            'title_page_title',
            'spine_title',
            'edition',
            'numbered_pages',
            'is_hardcover',
            'cover_color',
            'record_type',
            'subject_names',
            'summary',
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
