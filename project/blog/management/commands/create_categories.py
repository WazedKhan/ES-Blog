import random
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Category


class Command(BaseCommand):
    help = "Create a specified number of categories"

    def handle(self, *args, **options):
        fake = Faker()
        count = 20

        for _ in range(count):
            name = fake.word()
            slug = name.lower()

            Category.objects.create(name=name, slug=slug)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created category: {name}")
            )
