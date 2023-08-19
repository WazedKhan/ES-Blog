import random

from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from faker import Faker

from ...models import Category, BlogPost


class Command(BaseCommand):
    help = "Create a specified number of blog posts"

    def handle(self, *args, **options):
        fake = Faker()
        count = 30000
        users = User.objects.all()
        categories = Category.objects.all()

        for _ in range(count):
            title = fake.sentence()
            content = fake.paragraphs(5)
            author = random.choice(users)
            category = random.choice(categories)
            date_published = date_published = fake.date_time_this_year(
                tzinfo=timezone.utc
            )  # Make the datetime timezone-aware

            post = BlogPost.objects.create(
                title=title,
                content="\n".join(content),
                author=author,
                date_published=date_published,
            )
            post.categories.set(random.sample(list(categories), random.randint(1, 3)))
            self.stdout.write(self.style.SUCCESS(f"Successfully created post: {title}"))
