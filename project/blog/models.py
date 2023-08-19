from django.db import models
from django.contrib.auth.models import User


class TimestampedModel(models.Model):
    """
    An abstract base model that includes timestamp fields for creation and update.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    """
    Represents a category for blog posts.
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPost(TimestampedModel):
    """
    Represents a blog post.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Comment(TimestampedModel):
    """
    Represents a comment on a blog post.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Reaction(TimestampedModel):
    """
    Represents a user reaction to a blog post or comment.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, blank=True, null=True
    )
    reaction_type = models.CharField(max_length=10)  # 'like', 'dislike', 'haha', 'sad'

    def __str__(self):
        return f"Reaction by {self.user.username}"
