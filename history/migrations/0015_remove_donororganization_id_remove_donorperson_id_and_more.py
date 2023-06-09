# Generated by Django 4.2 on 2023-04-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0014_inventoryitem_donated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donororganization',
            name='id',
        ),
        migrations.RemoveField(
            model_name='donorperson',
            name='id',
        ),
        migrations.AddField(
            model_name='donororganization',
            name='donor_organization_id',
            field=models.CharField(default='2ZWkDCEDVoW4EhPq2r3RFnXgsc77kzBMOSlQoHcADJ5qB9Hn8735YURE2GRSVkaaOVcYqH88qMpHppKrAn327EvzCFybgksLhrP91oLWN3bcIk7HCltUjTboO1MxJJrM', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='donorperson',
            name='donor_person_id',
            field=models.CharField(default='54O6O8KhGDg1V7PbxmT3QQyPSvyVdB0LVrJs6vnx5Y1A20fFvxX9nRhOMfyrATx00XVibh6F3nzxNzPRloRjZabhkkgBgNOh6pFBCsqLOpsTG9WiLjtc3hJcTFm9x2AZ', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventoryimage',
            name='inventory_image_id',
            field=models.CharField(default='aqvn13krzrkERrgdLnuCcpMCrvObGaYqEwChMpWcD1bnVeY6Ao3iXCgVX6Eav8hJ79H4XRWQxcPmSVHy6W8erqNEst4KoJNH9aWKMrmSn7zBZormCDlIJcXZAUxvu5uJ', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='inventory_item_id',
            field=models.CharField(default='qd58VqWVXxyOj3iU4SOq1P0fAn8FQeLUbY6ZHXiUMuiY34V1nt4J1P22by8XFakICqRLsw5j9wOtpXmIa5k8tODOZgn4jJeFjPXzB3YxqFX1j0lKitB0ciHuoKRgYNXz', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventorylocation',
            name='inventory_location_id',
            field=models.CharField(default='UgHOZzvWMbbaHiqtQpYPylkkyZwmuE7sHkGBBMtzcopFfbU3nJPucz8TUDbEaJ8IfVlMQ4KQXv3qZ728lLWPntriwrWdw12oyTWMOHBuuMwC8ej0Kycrzggy3SBn91FF', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventorylocationassign',
            name='inventory_location_assign_id',
            field=models.CharField(default='HOMNqGr3Hi2K2ykcp3mfbqLNrGF0IAJE7cBQT5M0FxsuIiVrpzqNfsa4hZkyLv1RZEEMJ2uMA3CCnQ1BXyFugHXG8f6A1Sf5rlSEjNcjcm6IAqc2nlNhfLpaJXRorisk', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventorystatus',
            name='inventory_status_id',
            field=models.CharField(default='mfNsfqtOAu90kNOMXrM58tzhpt6qiiVTcuGr0GDgTiLjT2TxDIJ05KNX2IKa9TQE4I8FoaPbTD17Ae36jTQATqqiEUrlruDUPLSP6NmfOaNnw4UgGFyw9l96L710dsHp', max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventorystatusassign',
            name='inventory_status_assign_id',
            field=models.CharField(default='2Vi8L05hFJOlgWMUxeCh7iqgQuamEajcuGYzVuWu7HnS64lJmAb7CunjRI9kcVX2AQaMTH9FqVcRGTQGvdegcuPHIxkyNpchbNd81urmiJG05biEQtDnk8PLDtafDq5f', max_length=128, primary_key=True, serialize=False),
        ),
    ]
