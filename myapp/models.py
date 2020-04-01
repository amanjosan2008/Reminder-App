from django.db import models

class user(models.Model):
    name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40, default = 'Kapurthala')
    phone = models.CharField(max_length = 14, unique = True)

    def __str__(self):
        return self.name
