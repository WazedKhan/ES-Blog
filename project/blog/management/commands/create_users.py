from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

from faker import Faker


class Command(BaseCommand):
    help = "Create thousands of users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Number of users to create")

    def handle(self, *args, **options):
        fake = Faker()
        count = options["count"]
        for _ in range(count):
            username = fake.user_name()
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = "password123"
            try:
                User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created user: {username}")
                )
            except IntegrityError:
                self.stdout.write(self.style.WARNING(f"{username} Already Exists!"))
