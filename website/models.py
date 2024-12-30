from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=15, unique=True)  # Assuming roll numbers are unique
    email = models.EmailField(unique=True)  # Assuming email addresses are unique
    
    def __str__(self):
        return self.name
