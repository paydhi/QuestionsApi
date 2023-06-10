from rest_framework import serializers

from questions.models import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    jservice_id = serializers.IntegerField()
    answer = serializers.CharField()
    question = serializers.CharField()
    jservice_created_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Questions
        fields = '__all__'


class QuestionsPostSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField(required=True, min_value=1)

    class Meta:
        fields = ['questions_num']
