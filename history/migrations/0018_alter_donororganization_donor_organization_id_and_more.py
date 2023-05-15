# Generated by Django 4.2 on 2023-05-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0017_remove_inventoryitem_inventory_category_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donororganization",
            name="donor_organization_id",
            field=models.CharField(
                default="7UnwfLDbkwbUszHkSGU2d0ax3kXX40cWsOaAe7KWTomNNriXBaHDGtQP9RTA6mA62sLwMecKpGRs3aIPwKHFcOfUCPUiUYBpGlDcu9pMXAuzg7leJmWSZjw2hrxoud",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="donororganization",
            name="user_key_create",
            field=models.CharField(
                default="6BAzvgtAuHNGN9Ti9Z3XthKYb9aUFAAJu7ObKzQGPgYirEec4WgBgTRACgSfGiK03BPD2xsDkP3rTiog0tYF50ZZhVqGfwtbESaqolqVD6dsDqE6N5ML1YtTt9w6bj",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="donorperson",
            name="donor_person_id",
            field=models.CharField(
                default="UaOpkmA4Gs9PiGtDV77Bu4UlOPOVE9luiTHNpwD85w6r7xSlX3xKKPdd6iFq1qWp66MTrylA5N8SZXmQqSZfhJq0D4KdeULP4wlj1xytCjWJz8aaQRlYgKCZDBoe5x",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="donorperson",
            name="user_key_create",
            field=models.CharField(
                default="6BAzvgtAuHNGN9Ti9Z3XthKYb9aUFAAJu7ObKzQGPgYirEec4WgBgTRACgSfGiK03BPD2xsDkP3rTiog0tYF50ZZhVqGfwtbESaqolqVD6dsDqE6N5ML1YtTt9w6bj",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="giftagreement",
            name="gift_agreement_id",
            field=models.CharField(
                default="T5qFFwgN4bpDdwxymrjPfuNSJ7Y1jnZyAJouxpsidaSpQTIdna0X9Dy5nPinHPkH2p26YMlGmf39aQlZW3dYhaDtBCg2Mw6fRk0qVbzwgGoG7IZ5GuSZVUPlLYGEnf",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="giftagreement",
            name="gift_agreement_number",
            field=models.CharField(
                default="udDMzbknss6rWyMuCntrsliAdwvIVNWyp1OqxnRCMfjAuf74V4QrKmXoJnM7rEOjunJtCWk7W8KDrWhAxhFhaTnncw3m49SS31bGhg0EeNFClZZtwG1FR4ie20z53d",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryimage",
            name="inventory_image_id",
            field=models.CharField(
                default="IG3aaFjonCoyryTlsq7klsF7ciwsvw7I8I4U2XbdG4IHdcKlWWCQCl9T6Skh89cdLDVVnB8WZ5MZmbXpOEgyrLs4BSOoVtps3QHkSOaPW42TtXWODXiOvX2TfZE93C",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="accession_id",
            field=models.CharField(
                default="", help_text="unique identifier, eg. ISBN", max_length=32
            ),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="height",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="inventory_item_id",
            field=models.CharField(
                default="kypSIrqZtaenKGZT0Krg45FzanZZavrdzCETbObANUSvsDbscG2LOq5IMdOmZ1XkdMXrnsbk4WGTWhb69JjRTLfwfUAq0VRr1Mp7kmpeCwsF4rHNRdCxg8wtzPqopr",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="length",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="manufactured_in",
            field=models.CharField(default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="user_key_create",
            field=models.CharField(default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="width",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="inventorylocation",
            name="inventory_location_id",
            field=models.CharField(
                default="JwNnahssDpu2iKOQEpsfI5dWqRD4Hr0po17ig9hRlyvS6ZiNhkXqyqvBqyqvs03OcqqrRfVkFI8Gvwopkpwj06Bhi6N5CgU9jvztUVxySzgDtMuw0UtKoDCRIapRbL",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorylocationassign",
            name="inventory_location_assign_id",
            field=models.CharField(
                default="CCvQevqakXlhGs6gkgGZjZCZ1Kykf45cq46klq2eqaFxlBVe5WCE98lvFzuxktnhenNr6vaJlp2xM0JdRa90dSHwzF6HqlijplLYJPKParMHpE61LGgwV8H6eRhLyC",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorynote",
            name="inventory_note_id",
            field=models.CharField(
                default="xqsqHb2HZnfJwyQxY1hmC6mcKKqB2lZanaiKfj2KBQUGK6JDitBVUpU2CvIz7lA5PvnRP2VDrrfbi6ndJFhUa5SmTpumkFGpWR8DLXLMLNWA0lJBs9lyFBlAhpQdkk",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryownership",
            name="inventory_ownership_id",
            field=models.CharField(
                default="ZZ5b7sWHdqHP8GD0pn5ifkqIfZ9dDuXQF2716prGILURrKJdd9cSRjf59C3nakoereFDabE7R7inVgELYdj8ANYCgOdPt8HXITA5A7LjheHcF1mzd2mJcCwFXFIqvL",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorystatus",
            name="inventory_status_id",
            field=models.CharField(
                default="LXz1lo0FZRuObikKSGxVBRdT9juUvo1V8iCPw84CzCr3nBCJiP0Nmv29l9z8FTQiGhggAcjZP5E3mrAs51h6MadMny01UfFxsa6qIh0wgaJnyAgiGumiX193VupVOv",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorystatusassign",
            name="inventory_status_assign_id",
            field=models.CharField(
                default="oXWMWAuOk54Wy0RY7zJRP4FyAlQX7SXSogWJoheDdGa99CXaQQp8CDYSCU6pMTc4McsicfJultkxf8H0GzR3PFRf6Q1Z34ogXrGwSorWk29vPs0xrJwNLEYwlInBzB",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="manufacturer_id",
            field=models.CharField(
                default="2GKadNSfhLDve3j1i784R9F4O7nAprYFHx5HFL22AlXcbF5NCiHtij4agXn4OxgTGokbEevHeUg14SPzrLiFu9Y4hUbgpGGIdq3YJAJ7FR2fmD0q360wWG7tId7hdy",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="ownerorganization",
            name="owner_organization_id",
            field=models.CharField(
                default="ENCJQu3CLY2mNY9ViaLIAHYeR7rBJgtDKwH0plSTgOQTwwtC6og8Uwmtnd7QtJh6PI64cSeJmS1zHWnurTVEGDNL75eH8WQjalrYNm4cOVzonHmulqZaDFQXzqXtNl",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="ownerorganization",
            name="user_key_create",
            field=models.CharField(
                default="Uv9L4Z5Da2r7SQLeHMbHlkzic4L8Y3gLLzqlBcliRPuLNqAWFXBzh1JknwfSsScliDCT2HavQzYoByc6xGDGJZQwIryNNx3NxqU2l6oaS635USftp2ixiDTsvULthW",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="ownerperson",
            name="owner_person_id",
            field=models.CharField(
                default="d7vCcdHiihy2nI50qHQ5mDp3frOT5WO1U1y7eBJNrOtdrm4Lvwobmm2RrOT3JYKiBMf3HJcpNw0mHuKhT5eTCOphhW6a3ckopsyT9NuGNLReLpPFJCP69HlyfHy3E2",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="ownerperson",
            name="user_key_create",
            field=models.CharField(
                default="Uv9L4Z5Da2r7SQLeHMbHlkzic4L8Y3gLLzqlBcliRPuLNqAWFXBzh1JknwfSsScliDCT2HavQzYoByc6xGDGJZQwIryNNx3NxqU2l6oaS635USftp2ixiDTsvULthW",
                max_length=128,
            ),
        ),
    ]