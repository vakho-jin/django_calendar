from django.db import models

class Calendar(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

