from rest_framework.serializers import ModelSerializer

from users.models import User


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
