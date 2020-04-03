from django.db import models

class user(models.Model):
    name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40, default = 'Kapurthala')
    phone = models.CharField(max_length = 10, unique = True)

    def __str__(self):
        return self.name

class message_format(models.Model):
    message_text = models.TextField(max_length = 200)

    def __str__(self):
        return self.message_text
