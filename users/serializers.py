from datetime import date

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User, Contributor


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'birthdate',
            'can_be_contacted',
            'can_data_be_shared'
        ]

    """def validate_birthdate(self, value):
        today = date.today()
        age = today.year - value.year

        if (today.month, today.day) < (value.month, value.day):
            age -= 1"""


class ContributorSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contributor
        fields = ['user']
