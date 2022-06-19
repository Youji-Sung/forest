from rest_framework import serializers
from django.contrib.auth import get_user_model

from community.serializers import User
from .models import Forest, Review, Community

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta :
            model = User
            fields = ('nickname','username','id')
    
    user = UserSerializer(read_only=True)
    
    class ForestSerializer(serializers.ModelSerializer):
        class Meta :
            model = Forest
            fields = '__all__'

    forest = ForestSerializer(read_only=True)

    class Meta :
        model = Review
        fields = '__all__'



class CommunitySerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta :
            model = User
            fields = ('nickname','username','id')
    
    user = UserSerializer(read_only=True)
    
    class ForestSerializer(serializers.ModelSerializer):
        class Meta :
            model = Forest
            fields = '__all__'

    forest = ForestSerializer(read_only=True)

    class Meta :
        model = Community
        fields = '__all__'



class ForestSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only=True, many=True)
    communitys = CommunitySerializer(read_only=True, many=True)

    class Meta :
        model = Forest
        fields = '__all__'



class ForestListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Forest
        fields = '__all__'
