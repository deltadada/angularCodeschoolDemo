from rest_framework import serializers
from gemstore.models import Gems, Reviews
from gemstore.models import ThumbDisplays

from gemstore.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class Gems2Serializer(serializers.Serializer):
    class Meta:
        model = Gems
        fields = ('name', 'price','description')

class ThumbDisplays2Serializer(serializers.Serializer):
    class Meta:
        model = ThumbDisplays
        fields = ('url', 'name', 'description','price')


class ThumbsDisplaySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    url = serializers.CharField(max_length = 2000, required=True )
    name = serializers.CharField(max_length = 255, required=True )
    price = serializers.DecimalField(max_digits=10, decimal_places=2,required=True,)
    description = serializers.CharField(max_length = 1056, required=False )

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Gems` instance, given the validated data.
    #     """
    #     return Gems.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Gems` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.gem)
    #     instance.price = validated_data.get('price', instance.gem)
    #     instance.description = validated_data.get('description', instance.gem)
    #     instance.canPurchase = validated_data.get('canPurchase', instance.gem)
    #     instance.save()
    #     return instance

class GemsSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 255, required=True )
    price = serializers.DecimalField(max_digits=10, decimal_places=2,required=True,)
    description = serializers.CharField(max_length = 1056, required=False )
    canPurchase = serializers.BooleanField(required=False)
    #url = serializers.URLField(max_length = 2000, default="assets/img/noImage_th.png" )

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Gems` instance, given the validated data.
    #     """
    #     return Gems.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Gems` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.gem)
    #     instance.price = validated_data.get('price', instance.gem)
    #     instance.description = validated_data.get('description', instance.gem)
    #     instance.canPurchase = validated_data.get('canPurchase', instance.gem)
    #     instance.save()
    #     return instance

class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance