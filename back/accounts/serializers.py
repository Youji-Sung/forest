from forests.models import Forest
from forests.serializers import ForestSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=20)
    profile_image = serializers.ImageField(use_url=True, required=False, default='/profile/None.png')
    date_of_birth = serializers.DateField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['profile_image'] = self.validated_data.get('profile_image', '')
        data['date_of_birth'] = self.validated_data.get('date_of_birth', '')
        return data

    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2','nickname','profile_image','date_of_birth')


    

class ProfileSerializer(serializers.ModelSerializer):
    
    class ForestSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Forest
            fields = ('pk', 'name')

    like_forests = ForestSerializer(many=True,read_only=True)
    stamp_forests = ForestSerializer(many=True,read_only=True)
    
    class Meta :
        model = get_user_model()
        fields = ('pk','username','profile_image','nickname','email','date_of_birth','like_forests','stamp_forests')