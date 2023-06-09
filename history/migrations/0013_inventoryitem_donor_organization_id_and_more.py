# Generated by Django 4.2 on 2023-04-23 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0012_donororganization_donorperson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='donor_organization_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.donororganization'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='donor_person_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.donorperson'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='inventory_status_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.inventorystatus'),
        ),
        migrations.AlterField(
            model_name='inventorylocationassign',
            name='inventory_item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.inventoryitem'),
        ),
        migrations.AlterField(
            model_name='inventorylocationassign',
            name='inventory_location_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.inventorylocation'),
        ),
        migrations.AlterField(
            model_name='inventorystatusassign',
            name='inventory_item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.inventoryitem'),
        ),
        migrations.AlterField(
            model_name='inventorystatusassign',
            name='inventory_status_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.inventorystatus'),
        ),
    ]
