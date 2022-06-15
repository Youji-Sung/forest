from rest_framework import serializers
from django.contrib.auth import get_user_model
from forests.models import Forest
from forests.serializers import ForestSerializer

class ProfileSerializer(serializers.ModelSerizlizer):
    
    class ForestSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Forest
            fields = ('pk', 'name')

    like_forests = ForestSerializer(many=True)
    stamp_forest = ForestSerializer(many=True)
    
    class Meta :
        model = get_user_model()
        fields = ('pk','username','profile_image','nickname','date_of_birth','like_forests','stamp_forest')