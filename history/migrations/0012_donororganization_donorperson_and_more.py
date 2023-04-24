# Generated by Django 4.2 on 2023-04-23 08:24

from django.db import migrations, models
import django.db.models.deletion
import history.models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0011_alter_inventoryimage_inventory_image_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(help_text='street address', max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('province_state', models.CharField(help_text='province/state/region', max_length=64)),
                ('country', models.CharField(default=history.models.Country['CANADA'], max_length=32)),
                ('phone_area_code', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=7)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user_key_create', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonorPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(help_text='street address', max_length=128)),
                ('city', models.CharField(max_length=64)),
                ('province_state', models.CharField(help_text='province/state/region', max_length=64)),
                ('country', models.CharField(default=history.models.Country['CANADA'], max_length=32)),
                ('phone_area_code', models.CharField(max_length=3)),
                ('phone_number', models.CharField(max_length=7)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user_key_create', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='inventoryimage',
            name='inventory_item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.inventoryitem'),
        ),
    ]
