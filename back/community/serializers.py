
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta :
            model = User
            fields = ('nickname',)

    
    user = UserSerializer(read_only=True)

    class Meta :
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta :
            model = User
            fields = ('nickname',)

    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta :
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta :
            model = User
            fields = ('nickname',)

    user = UserSerializer(read_only=True)

    class Meta :
        model = Article
        fields = ('pk', 'user', 'title', 'article_image',)