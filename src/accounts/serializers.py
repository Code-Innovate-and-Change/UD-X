from django.contrib.auth.models import User 
from rest_framework import serializers 
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=70)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only = True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User 
        fields = ["email","first_name","last_name","password","password2"]


    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        
# Check if email exists already
        if email_exists:
            raise ValidationError({"email": "Email already exists"})

# Check if the passwords match
        if attrs["password"] !=  attrs["password2"]:
            raise ValidationError({"password": "Password do not match"})
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        # Remove password2 from validated_data
        validated_data.pop('password2')
        validated_data['username'] = validated_data['email']

        user = User.objects.create_user(**validated_data) 

        return user
    