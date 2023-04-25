from django.db import models
from history.util.model_utils import randomId

class InventoryNote(models.Model):
    inventory_note_id = models.CharField(max_length=128, primary_key=True, default=randomId())
    inventory_item_id = models.ForeignKey('InventoryItem', on_delete=models.SET_NULL, null=True)
    user_key_create = models.CharField(max_length=128, default=None)
    created_at = models.DateTimeField(auto_now=True)
    note = models.TextField()

