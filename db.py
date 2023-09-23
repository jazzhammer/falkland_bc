from history.entity.donor import DonorPerson
DonorPerson.objects.create(
    street="street",
    city="city",
    province_state="ab",
    country="can",
    phone_area_code="234",
    phone_number="9873737",
    last_name="last_name",
    first_name="first_name"
)

DonorPerson.objects.create(
    street="street1",
    city="city1",
    province_state="ab",
    country="can",
    phone_area_code="255",
    phone_number="9873937",
    last_name="last_name1",
    first_name="first_name1"
)
