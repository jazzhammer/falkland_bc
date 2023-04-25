from django.db.models import *
from history.util.model_utils import randomId

class Manufacturer(Model):
    manufacturer_id = CharField(max_length=128, primary_key=True, default=randomId())
    name = CharField(max_length=128)
    url = URLField(default='')
