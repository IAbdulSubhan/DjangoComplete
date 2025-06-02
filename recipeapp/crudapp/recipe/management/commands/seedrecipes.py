from django.core.management.base import BaseCommand
from faker import Faker
from recipe.models import Recipe

fake = Faker()

class Command(BaseCommand):
    help =  "Seed the database with fake recipes"

    def handle(self, *args, **kwargs):
        for _ in range(10):
            title = fake.sentence(nb_words=3)
            description = fake.text()
            Recipe.objects.create(
                title= title,
                description= description
            )

    self.stdout.write(self.style.SUCCESS("Seeded 10 recipes"))