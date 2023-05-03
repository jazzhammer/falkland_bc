from history.util.model_utils import randomId
from django.db.models import *

class InventoryCategory(Model):
    inventory_category_id = CharField(max_length=128, primary_key=True, default=randomId())
    name = CharField(max_length=128, null=False)
    user_key_create = CharField(max_length=128, default=None)
    created_at = DateTimeField(auto_now=True)
    image = ImageField(upload_to='images/inventory', default=None)

