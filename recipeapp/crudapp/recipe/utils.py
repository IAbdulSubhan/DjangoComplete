from django.utils.text import slugify
import uuid 
from .models import Recipe


def generate_slug(title: str)->str:
    
    slug = slugify(title)

    while(Recipe.objects.filter(slug=slug).exists):
        slug = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'
    return slug