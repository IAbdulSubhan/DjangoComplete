from django.utils.text import slugify
import uuid


def generate_slug(title: str) -> str:
    from .models import Recipe
    base_slug = slugify(title)
    slug = base_slug
    while Recipe.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{str(uuid.uuid4())[:4]}"
    return slug
