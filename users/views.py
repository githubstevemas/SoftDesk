from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UsersSerializer


class UsersViewset(ModelViewSet):
    serializer_class = UsersSerializer

    def get_queryset(self):
        return User.objects.all()
