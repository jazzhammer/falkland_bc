# Generated by Django 4.2 on 2023-04-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0013_inventoryitem_donor_organization_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='donated_at',
            field=models.DateTimeField(null=True),
        ),
    ]