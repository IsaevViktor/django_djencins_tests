from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __eq__(self, other):
        return self.name == other.name and self.password == other.password

    def __str__(self):
        return self.name + ' ' + self.password


