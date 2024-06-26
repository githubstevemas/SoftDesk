from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UsersViewset


router = routers.SimpleRouter()
router.register('users', UsersViewset, basename='users-list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
