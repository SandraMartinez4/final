from rest_framework import serializers

class EvalSerializer(serializers.Serializer):
    expression = serializers.CharField()
    variables = serializers.DictField(child=serializers.FloatField(), required=False)