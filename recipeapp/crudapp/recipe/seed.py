import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crudapp.settings")
django.setup()



def recipe_generator():
    from recipe.models import Recipe
    fake = Faker()
    for _ in range(10):
        title = fake.sentence(nb_words = 3)
        description = fake.text()
        recipe = Recipe.objects.create(title= title, description=description)
        print(f'created: {recipe.title}')

    print(f'Completed the seed data {recipe}')
