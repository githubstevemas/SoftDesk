from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectsSerializer


class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Project.objects.all()
