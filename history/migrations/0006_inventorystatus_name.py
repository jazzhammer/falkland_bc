# Generated by Django 4.2 on 2023-04-23 05:36

from django.db import migrations, models
import history.models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_alter_inventoryitem_inventory_item_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorystatus',
            name='name',
            field=models.CharField(default=history.models.StatusName['NEW'], verbose_name=128),
        ),
    ]
