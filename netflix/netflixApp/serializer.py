from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.exceptions import ValidationError

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'movie', 'text']
    def Validate_text(self, qiymat):
        if "yaramas" in qiymat:
            raise ValidationError(f"Bu so'zni{qiymat} ishlatish mumkin emas")
        return qiymat