from django.urls import path, include
from rest_framework import routers

from ..views.blog import UserViewSet, CategoryViewSet, BlogPostViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)
router.register("category", CategoryViewSet)
router.register("blog", BlogPostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
