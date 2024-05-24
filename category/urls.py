from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet
)
from django.urls.conf import include, path

router = DefaultRouter()

router.register(r'', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
