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


class ContributorSerializer(ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Contributor
        fields = ['user']
