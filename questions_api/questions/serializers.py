from rest_framework import serializers

from questions.models import Questions


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ['id', 'jservice_id', 'answer', 'question', 'question_created_at']
