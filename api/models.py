from django.db import models
from datetime import date

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
    # Calculate age automatically
    @property
    def age(self):
        today = date.today()
        age_calculated = today.year - self.date_of_birth.year
        
        # Check if birthday hasn't happened this year
        if (today.month < self.date_of_birth.month) or \
           (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age_calculated -= 1
            
        return age_calculated
    
    def __str__(self):
        return f"{self.name} - {self.age} years old"