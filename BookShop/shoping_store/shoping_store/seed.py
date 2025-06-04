import os
import django
from faker import Faker
from books.models import Book


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoping_store.settings')
django.setup()

fake = Faker()
def seed_books():
    for _ in range(10):
        name = fake.sentence(nb_words= 4)
        author = fake.name()
        price = fake.random_int(100, 1000)
    
        Book.objects.create(
            name=name,
            author = author,
            price = price
        )

    print("Seeded 10 Books")

