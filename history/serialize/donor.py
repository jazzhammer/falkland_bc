from rest_framework import serializers
from history.entity.donor import DonorPerson


class DonorPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorPerson
        fields = (
            'donor_person_id',
            'street',
            'city',
            'province_state',
            'country',
            'phone_area_code',
            'phone_number',
            'last_name',
            'first_name',
            'created_at',
            'user_key_create'
        )


class CreateDonorPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorPerson
        fields = [
            'street',
            'city',
            'province_state',
            'country',
            'phone_area_code',
            'phone_number',
            'last_name',
            'first_name'
        ]