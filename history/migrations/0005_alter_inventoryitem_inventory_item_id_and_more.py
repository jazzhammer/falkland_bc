# Generated by Django 4.2 on 2023-04-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_inventorystatus_remove_inventoryitem_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='inventory_item_id',
            field=models.CharField(default=None, primary_key=True, serialize=False, verbose_name=128),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='status_id',
            field=models.CharField(default=None, verbose_name=128),
        ),
    ]
