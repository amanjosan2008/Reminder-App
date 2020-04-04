from django.db import models

class user(models.Model):
    name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40, default = 'Kapurthala')
    phone = models.IntegerField(unique = True)
    added_time = models.DateTimeField(auto_now_add=True)
    #last_sms = models.DateTimeField(auto_now=True)
    last_sms = models.DateTimeField(blank=True, null=True)
    success = models.IntegerField(default=0, blank=True)
    error = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

class message_format(models.Model):
    message_text = models.TextField(max_length = 200)

    def __str__(self):
        return self.message_text
