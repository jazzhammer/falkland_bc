from history.util.model_utils import randomId
from django.db.models import *

class GiftAgreement(Model):
    gift_agreement_id = CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = ForeignKey('InventoryItem', on_delete=SET_NULL, null=True)
    user_key_create = CharField(max_length=128, default=None)
    created_at = DateTimeField(auto_now=True)

