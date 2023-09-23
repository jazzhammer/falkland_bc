from django.db import models
from django.db.models import *


class Country(models.Model):
    name = CharField(max_length=64)
    alpha_2 = CharField(max_length=64)
    alpha_3 = CharField(max_length=64)
    country_code = CharField(max_length=64)
    iso_3166_2 = CharField(max_length=64)
    region = CharField(max_length=64)
    sub_region = CharField(max_length=64)
    intermediate_region = CharField(max_length=64)
    region_code = CharField(max_length=64)
    sub_region_code = CharField(max_length=64)
    intermediate_region_code = CharField(max_length=64)

    default_number = "124"
