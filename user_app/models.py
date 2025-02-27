from django.db import models
from datetime import date

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    birth_date = models.DateField()

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def __str__(self):
        return f"სახელი: {self.first_name}, გვარი: {self.last_name}. ასაკი: {self.age()}"