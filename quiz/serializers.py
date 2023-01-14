from rest_framework import serializers
from .models import Quiz

class QuizSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')
