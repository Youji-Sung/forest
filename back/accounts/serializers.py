from rest_framework import serializers
from django.contrib.auth import get_user_model
from forests.models import Forest
from forests.serializers import ForestSerializer


from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers


# 새로 생성(5/24)
class UserSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=20)
    profile_image = serializers.ImageField(use_url=True)
    date_of_birth = serializers.DateField()

    # def get_cleaned_data(self):
    #     data = super().get_cleaned_data()
    #     data['nickname'] = self.validated_data.get('nickname', '')
    #     # data['profile_image'] = self.validated_data.get('profile_image', '')
    #     return data

class ProfileSerializer(serializers.ModelSerializer):
    
    class ForestSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Forest
            fields = ('pk', 'name')

    like_forests = ForestSerializer(many=True)
    stamp_forest = ForestSerializer(many=True)
    
    class Meta :
        model = get_user_model()
        fields = ('pk','username','profile_image','nickname','date_of_birth','like_forests','stamp_forest')