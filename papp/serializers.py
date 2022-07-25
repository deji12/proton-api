from pyexpat import model
from rest_framework import serializers 
from .models import Note, Profile, GeneratePassword, DeveloperMode
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class GeneratePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratePassword
        fields = '__all__'

class DeveloperModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperMode
        fields = '__all__'