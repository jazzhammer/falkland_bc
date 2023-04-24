# Generated by Django 4.2 on 2023-04-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, verbose_name=128)),
                ('name', models.CharField(verbose_name=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
