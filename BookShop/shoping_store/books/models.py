from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(default="", max_length=50)
    price = models.IntegerField(default=0)
    book_image = models.ImageField(upload_to="books/")
    

    def __str__(self):
        return self.name

