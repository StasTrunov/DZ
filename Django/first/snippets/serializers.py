from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLES_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(requiared = True, max_length = 250)
    code = serializers.CharField(style = {'base_template': 'textarea.html'})
    language = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default = 'python')
    language = serializers.ChoiceField(choices = STYLES_CHOICES, default = 'igor')

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    def create(self, instance, validated_data):
        instance.title = validated_data.get('tittle', instance.title)
        

        return Snippet.objects.create(**validated_data)    
