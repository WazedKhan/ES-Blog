from django.db.models import Prefetch

from django.contrib.auth.models import User

from rest_framework import viewsets

from blog.models import Category, BlogPost
from ..serializers.blog import CategorySerializer, BlogSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = BlogPost.objects.none()

    def get_queryset(self):
        queryset = BlogPost.objects.prefetch_related("author", "categories").only(
            "id",
            "author__id",
            "author__username",
            "author__first_name",
            "author__last_name",
            "categories__id",
            "categories__name",
            "categories__slug",
            "created_at",
            "updated_at",
            "title",
            "content",
            "date_published",
        )
        return queryset
