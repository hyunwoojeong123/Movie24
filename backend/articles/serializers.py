from rest_framework import serializers
from .models import Article,Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'user', 'read', 'comments_cnt',)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','content','user')
        read_only_fields = ('article',)

class CommentSerializerForProfile(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','content','user', 'article')

class CommentSerializerForComments(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','content','user', 'username')
        
