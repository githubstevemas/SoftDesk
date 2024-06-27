from rest_framework.serializers import ModelSerializer

from projects.models import Project
from users.serializers import UsersSerializer, ContributorSerializer


class ProjectsSerializer(ModelSerializer):

    author = UsersSerializer()
    contributors = ContributorSerializer()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'author',
            'contributors',
            'description',
            'type',
            'created_time'
        ]
