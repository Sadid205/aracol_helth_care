from rest_framework import serializers 
from .user_role_choices import ROLE

class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=14)
    user_role = serializers.CharField(max_length=10)

    def vlaidate_user_role(self,value):
        if not value:
            raise serializers.ValidationError("Please select a role!")
    def validate_phone(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must be contain only digits.")
        if len(value) < 11:
            raise serializers.ValidationError("Phone number must be at least 11 digits long.")
        return value