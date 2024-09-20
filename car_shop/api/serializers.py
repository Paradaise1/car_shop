from rest_framework import serializers

from shop.models import Car, Comment


class CarSerializer(serializers.ModelSerializer):
    '''Serializer for creating, modifying and deleting a car object.'''
    owner = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Car
        exclude = ('created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    '''Serializer for creating a comment object.'''
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    car = serializers.SlugRelatedField(
        read_only=True, slug_field='make'
    )

    class Meta:
        model = Comment
        exclude = ('created_at',)
        read_only_fields = ('car',)
