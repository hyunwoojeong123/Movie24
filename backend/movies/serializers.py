from rest_framework import serializers
from .models import Movie,Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','content', 'rating','user')
        read_only_fields = ('movie',)

class ReviewSerializerForReviews(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','content', 'rating','username')
        read_only_fields = ('movie',)