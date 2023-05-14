from history.util.model_utils import randomId
from django.db.models import *

class GiftAgreement(Model):
    gift_agreement_id = CharField(max_length=128, primary_key=True, default=randomId())
    gift_agreement_number = CharField(max_length=128, default=randomId())
    # the inventory_item related by inventory_item_id captures:
        # received_from
        # address
        # phone
        # disposal terms
            # eg. return to donor
            # eg. transferred to institution
            #
    inventory_item_id = ForeignKey('InventoryItem', on_delete=SET_NULL, null=True)
    user_key_create = CharField(max_length=128, default=None)
    created_at = DateTimeField(auto_now=True)

