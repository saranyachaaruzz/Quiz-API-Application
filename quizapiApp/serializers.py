from rest_framework import serializers
from .models import quiz

class quizSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiz
        fields = '__all__'

    def create(self,validated_data):
        return quiz.objects.create(**validated_data)


         





