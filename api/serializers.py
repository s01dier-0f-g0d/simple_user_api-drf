from rest_framework import serializers
from .models import UserProfile
from datetime import date

class UserProfileSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'date_of_birth', 'age']
        read_only_fields = ['id', 'age']
    
    def validate_date_of_birth(self, value):
        """Make sure date of birth is valid"""
        today = date.today()
        
        # Can't be born in the future
        if value > today:
            raise serializers.ValidationError("Date of birth can't be in the future!")
        
        # At least 1 year old
        age_check = today.year - value.year
        if (today.month < value.month) or (today.month == value.month and today.day < value.day):
            age_check -= 1
            
        if age_check < 1:
            raise serializers.ValidationError("Must be at least 1 year old")
            
        return value