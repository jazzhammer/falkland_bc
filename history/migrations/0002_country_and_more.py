# Generated by Django 4.2.5 on 2023-09-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("alpha_2", models.CharField(max_length=64)),
                ("alpha_3", models.CharField(max_length=64)),
                ("country_code", models.CharField(max_length=64)),
                ("iso_3166_2", models.CharField(max_length=64)),
                ("region", models.CharField(max_length=64)),
                ("sub_region", models.CharField(max_length=64)),
                ("intermediate_region", models.CharField(max_length=64)),
                ("region_code", models.CharField(max_length=64)),
                ("sub_region_code", models.CharField(max_length=64)),
                ("intermediate_region_code", models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name="donororganization",
            name="donor_organization_id",
            field=models.CharField(
                default="URq0L7P0kE2q5IjFxgpvpYtWbyzu7rgPQu8dQj0kiEwSqdSBzCr7jVNCApLQeRFDvWDDSEOdgWS0MAZFHOBWSn5vtnMD8w0Bfilztr7NMfKtxuMGd3Of3pJIKtaBAd",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="donororganization",
            name="user_key_create",
            field=models.CharField(
                default="ieO1Xrp1IUzTdScR4mwfCiokwoqAPKGlsDa7dYI6pAuy6qtUrbZRa8H9xN64Cb9VCZOaIGcEBNzPAIJ1qCEryYXpsjw5ZjdtviGuJbX9qy7qmQyagsR6jXxvqxbNCr",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="donorperson",
            name="donor_person_id",
            field=models.CharField(
                default="ucCmNKJUMQeQYuvL8rBAW2u5UTM2YDQkS5YD9AXma4L5ApoRxiXONYz5WH8PYsh0aC2JkhaplQFYuxE4c8yVqjb6oqYrsBBv4qvv8p47oDE64kKprVN71Pxd8yPYkY",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="donorperson",
            name="user_key_create",
            field=models.CharField(
                default="ieO1Xrp1IUzTdScR4mwfCiokwoqAPKGlsDa7dYI6pAuy6qtUrbZRa8H9xN64Cb9VCZOaIGcEBNzPAIJ1qCEryYXpsjw5ZjdtviGuJbX9qy7qmQyagsR6jXxvqxbNCr",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="giftagreement",
            name="gift_agreement_id",
            field=models.CharField(
                default="YZRPS4DxByyuKMgx3ZquMB1SN2ZjAJnK2H1sl02JVGhe95rKoLUFYo3IUy8ZTfEY0utasR4GDz6q9lxk9GLE50riF0q577AaWvnfVh6zp1rMNOEeJsXewGuWLvPzYE",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="giftagreement",
            name="gift_agreement_number",
            field=models.CharField(
                default="nhKrgFEKmya8CTE7JzcnCv4wfNLQqXp7ihLdbKDGAWlxlFGSM3nlgfvTW7ydYep0LWGFv84Xxp7OnjnuX0d5X6AsvkirMlNvOXbTiMRpg4ACdxlwUTaSyNipE8waUg",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryimage",
            name="inventory_image_id",
            field=models.CharField(
                default="gx9SxeIiWu5CYXh7OVwxDG1z6KsvaayvFIWOCSPl0PXBGZE17PPXcKhVzlvf3DSezUeJj4LIlAc7v6UWuMMOButjenCaB63AvNTtGrsofR1xMQD3v3LOrvFoAyn63v",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryitem",
            name="inventory_item_id",
            field=models.CharField(
                default="CGZF1ZLmBNnJLU8fQKlejR8zmtm8c3qirlOgittKFHvBBIrcug64BDPjoZi3Lrg4JIOMDGmhCRQFl7hK1Qfd8nuIUbqbERui7fG4oth5dvcRTU4XPFZzmvA5ua87Df",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorylocation",
            name="inventory_location_id",
            field=models.CharField(
                default="fjjNJCJDo0P1uqXziba0tFcKgUvrJxHtvNomyo34HmXGYNXRNdhfStlULw6QMAX65FtXhEOBBQzOV0w5e6ONbT9S1w86EOmUThhNvf1cMR88ZEKQtuyejTOme9yBTG",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorylocationassign",
            name="inventory_location_assign_id",
            field=models.CharField(
                default="CoD5LxZ8EbRNLOPVREKIiRCmImJRgizmOAXYPyO2PkRdXCTFEetoyFiHzfvK9n8USqyZQHPNm3lk6Wm9XiYxsce6iyTDTk4Pk3DGjOA4X2Q6ud80yCLmuB6mEeExiR",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorynote",
            name="inventory_note_id",
            field=models.CharField(
                default="DVPAqCwJnrPd6UnJ7N6EnkIOAmqIANoHHxPrdvXcCXMS9lfswalrc0pRbfDxmN66UwnADWXR14PZ9nXJdydJgxhpwgRvTMPyuANt9Si36VvOkYVwz5qor7Zg8GF2jl",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventoryownership",
            name="inventory_ownership_id",
            field=models.CharField(
                default="JKtuOyyTZserSdPnPiMSSIDsBMzdcBR2dMWRHOcdJrvwfKy8yiY83KWKYJFcKlbaMyOpppUKdL63XD2DV1omtlq8oojVpuWHWUKCbF9igBFnCRK1XjtEVJl5SJRNsG",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorystatus",
            name="inventory_status_id",
            field=models.CharField(
                default="78ykVBK2dazQ91IUVG55i8OYTwHIZXYtVgG1Yx35bCQjwCIxm0m6AQ09lnVc17Z0xGXKehejKaH7TNdjUiNpLpWT9MQquIv0V0G8j5AId3OZy5gf5duHYfeFm0BGpB",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="inventorystatusassign",
            name="inventory_status_assign_id",
            field=models.CharField(
                default="9zptHtcCsphRGlKlrM24kbd59I0dMYNilxMN4n9Yng13gHL53o4zwYzmqehE0Zp2Agy4E3WXEned6Zt4SnVzfkvAPNO8sWmnUhJKoAlrmSOC73sw4L9e9JjRUpa7lg",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="manufacturer_id",
            field=models.CharField(
                default="xT8738z0fsRBF8qPsXvAfjDmNnwfFqDLpW7wrPFnYroXlQk6YPjesbkY6IjcTDY5QJywNHg7nsjYD7l4VKLKD9rwYtldygnraCNOKsy7iRypacIa54eliI00mkDyTy",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="ownerorganization",
            name="owner_organization_id",
            field=models.CharField(
                default="uVqvsdBSlvD5Gqm5tmyDpkWU5yBfBw4rCgX9seAjESm6F6zTx969HGXb4S6WO2oM87pSMSRePA4kTBXX83163TAl07zVREjTiEAyjBbNszhPDIuPMEYBuJhMI4jgjH",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="ownerorganization",
            name="user_key_create",
            field=models.CharField(
                default="FsQ451W9yxC7kZXoglZAsfoPL7mrMUIkFNEcX78lfRRTIyaaUcWxdgP7zGxrdVr85gpW5i0ycnUySYYhsKlGDUa2uPd59ryGnH07Wp8nMMNGqvAjsIdRHzls85wGXl",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="ownerperson",
            name="owner_person_id",
            field=models.CharField(
                default="ZhB7LlU56lcF87N4AHG8rIMP5JEmWghsJDLQpumiFQlOvzuUOrXeIuF5mzQbOdscwNd4X1bFnIFONYpSgq1XgSwoJYdZ9ut8ND7vF0UYi05XsYCKvT6JEp0s6d8FtL",
                max_length=128,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="ownerperson",
            name="user_key_create",
            field=models.CharField(
                default="FsQ451W9yxC7kZXoglZAsfoPL7mrMUIkFNEcX78lfRRTIyaaUcWxdgP7zGxrdVr85gpW5i0ycnUySYYhsKlGDUa2uPd59ryGnH07Wp8nMMNGqvAjsIdRHzls85wGXl",
                max_length=128,
            ),
        ),
    ]