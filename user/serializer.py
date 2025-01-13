from rest_framework import serializers 
from .user_role_choices import ROLE

class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=14)
    role = serializers.CharField(max_length=10,choices=ROLE)

    def validate_phone(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must be contain only digits.")
        if len(value) < 11:
            raise serializers.ValidationError("Phone number must be at least 11 digits long.")
        return value