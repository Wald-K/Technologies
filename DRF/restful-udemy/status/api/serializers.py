from rest_framework import serializers
from status.models import Status


"""
serializer -> convert to json
serializer -> can validate data
"""

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

        read_only_fields = ['user']


    def validate_content(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Content to long")
        return value

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if image == "":
            image = None
        if content is None and image is None:
            raise  serializers.ValidationError("Content or image is required")
        return data
