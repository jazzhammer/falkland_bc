# Generated by Django 4.2 on 2023-04-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_inventoryitem_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryStatus',
            fields=[
                ('inventory_status_id', models.CharField(primary_key=True, serialize=False, verbose_name=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='id',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='inventory_item_id',
            field=models.CharField(default='', primary_key=True, serialize=False, verbose_name=128),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='status_id',
            field=models.CharField(default='', verbose_name=128),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='user_key_create',
            field=models.CharField(default=None, verbose_name=128),
        ),
    ]