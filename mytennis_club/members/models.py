from django.db import models
from datetime import date

# add a Member table by creating a Member class, and describe the table fields in it

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(default = 0)
    joined_date = models.DateField(default = date.today)


    def __str__(self):
        return f"FirstName: {self.firstname} LastName: {self.lastname}"
    
