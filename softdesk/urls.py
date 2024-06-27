from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UsersViewset
from projects.views import ProjectsViewset


router = routers.SimpleRouter()
router.register('users', UsersViewset, basename='users-list')
router.register('projects', ProjectsViewset, basename='projects-list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
