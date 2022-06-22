from telnetlib import LOGOUT
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET','PUT'])
def profile(request, username):
    user = get_object_or_404(User,username=username)

    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['DELETE'])
def user_delete(request,username):
    user = get_object_or_404(User,username=username)
    if request.user == user :
        user.delete()
        return Response('내가 사라져볼게 얍!')