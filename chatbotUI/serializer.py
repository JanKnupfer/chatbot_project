from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=180)

    # id = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = Question
        fields = ["question"]
