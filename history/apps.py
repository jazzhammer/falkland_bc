import json
import os
import psycopg2

from django.apps import AppConfig
from django.db.models import BigAutoField

from falkland_bc.settings import DATABASES
from history.util.path import appDir


class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'history'

    def ready(self):
        country_json = json.load(open(f'{appDir()}{os.path.sep}resource{os.path.sep}country-codes.js'))
        default_database = DATABASES['default']
        connection = psycopg2.connect(
            database=default_database['NAME'],
            host=default_database['HOST'],
            port=default_database['PORT'],
            user=default_database['USER'],
            password=default_database['PASSWORD']
        )
        readCursor = connection.cursor()
        for country in country_json:
            found = readCursor.execute(f"select count(id) from history_country where country_code = '{country['country-code']}'")

            if found == None:
                writeCursor = connection.cursor()
                name = country['name']
                if "'" in name:
                    name = name.replace("'", "''")
                valuesBlob = ""
                valuesBlob = valuesBlob + f"'{name}', "
                valuesBlob = valuesBlob + f"'{country['alpha-2']}', "
                valuesBlob = valuesBlob + f"'{country['alpha-3']}', "
                valuesBlob = valuesBlob + f"'{country['country-code']}', "
                valuesBlob = valuesBlob + f"'{country['iso_3166-2']}', "
                valuesBlob = valuesBlob + f"'{country['region']}', "
                valuesBlob = valuesBlob + f"'{country['sub-region']}', "
                if len(country['intermediate-region']) == 0:
                    valuesBlob = valuesBlob + f"'{country['intermediate-region']}', "
                else:
                    valuesBlob = valuesBlob + f"'{country['intermediate-region']}', "
                valuesBlob = valuesBlob + f"'{country['region-code']}', "
                valuesBlob = valuesBlob + f"'{country['sub-region-code']}', "
                if len(country['intermediate-region-code']) == 0:
                    valuesBlob = valuesBlob + f"'{country['intermediate-region-code']}'"
                else:
                    valuesBlob = valuesBlob + f"'{country['intermediate-region-code']}'"

                insert = f"""insert into history_country (
                    name,
                    alpha_2,
                    alpha_3,
                    country_code,
                    iso_3166_2,
                    region,
                    sub_region,
                    intermediate_region,
                    region_code,
                    sub_region_code,
                    intermediate_region_code
                ) values (
                    {valuesBlob}
                )"""
                writeCursor.execute(insert)
                writeCursor.close()
        readCursor.close()
        connection.close()