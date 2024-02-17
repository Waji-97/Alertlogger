from django.db import models

class Alert(models.Model):
    name = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    summary = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name