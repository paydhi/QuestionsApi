from rest_framework import serializers

from questions.models import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    jservice_id = serializers.IntegerField()
    answer = serializers.CharField()
    question = serializers.CharField()
    jservice_created_at = serializers.DateTimeField()

    class Meta:
        model = Questions
        fields = ['id', 'jservice_id', 'answer', 'question', 'jservice_created_at']


class QuestionsPostSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()

    class Meta:
        fields = ['questions_num']
