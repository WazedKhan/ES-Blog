from django.contrib.auth.models import User

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import BlogPost, Category, Comment


@registry.register_document
class UserDocument(Document):
    class Index:
        name = "blog_users"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = "blog_categories"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]


@registry.register_document
class BlogPostDocument(Document):
    author = fields.ObjectField(
        properties={
            "id": fields.IntegerField(),
            "username": fields.TextField(),
            "first_name": fields.TextField(),
            "last_name": fields.TextField(),
        }
    )
    categories = fields.ObjectField(
        properties={
            "id": fields.IntegerField(),
            "name": fields.TextField(),
            "slug": fields.TextField(),
        }
    )

    class Index:
        name = "blog_blog_posts"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = BlogPost
        fields = [
            "id",
            "created_at",
            "updated_at",
            "title",
            "content",
            "date_published",
        ]
