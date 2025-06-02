from django.db import models
from django.contrib.auth.models import User
from .utils import generate_slug

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    #blank=True → taake form se aane wali request mein required na ho
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

#🔸 Note: if not self.slug: ka matlab hai slug sirf tab generate ho jab pehli baar save ho raha ho (ya slug empty ho).
    def save(self, *args, **kwargs):
        print("Save called for:", self.title)
        if not self.slug:
            print("Slug is empty. Generating...")
            try:
                self.slug = generate_slug(self.title)
                print("Generated slug:", self.slug)
            except Exception as e:
                print(f"Slug Error: {e}")
        super().save(*args, **kwargs)




