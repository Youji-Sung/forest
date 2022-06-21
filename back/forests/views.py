from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Forest, Review, Community
from .serializers import ForestListSerializer, ForestSerializer, ReviewSerializer, CommunitySerializer

# Create your views here.
@api_view(['GET'])
def forests_list(request):
    forests = get_list_or_404(Forest)
    serializer = ForestListSerializer(forests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def forest_detail(request, forest_id):
    forest = get_object_or_404(Forest, pk=forest_id)
    serializer = ForestSerializer(forest)
    return Response(serializer.data)

@api_view(['POST'])
def like_forest(request, forest_id):
    forest = get_object_or_404(Forest, pk=forest_id)
    user = request.user
    if forest.like.filter(pk=user.pk).exists():
        forest.like.remove(user)
        serializer = ForestSerializer(forest)
        return Response(serializer.data)
    else:
        forest.like.add(user)
        serializer = ForestSerializer(forest)
        return Response(serializer.data)

@api_view(['POST'])
def stamp_forest(request, forest_id):
    forest = get_object_or_404(Forest, pk=forest_id)
    user = request.user
    if forest.stamp.filter(pk=user.pk).exists():
        forest.stamp.remove(user)
        serializer = ForestSerializer(forest)
        return Response(serializer.data)
    else:
        forest.stamp.add(user)
        serializer = ForestSerializer(forest)
        return Response(serializer.data)    

@api_view(['POST'])
def review_create(request, forest_id):
    user = request.user
    forest = get_object_or_404(Forest,pk=forest_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(forest=forest, user=user)
        reviews = forest.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, forest_id, review_pk):
    forest = get_object_or_404(Forest, pk=forest_id)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = forest.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = forest.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()   

@api_view(['POST'])
def community_create(request, forest_id):
    user = request.user
    forest = get_object_or_404(Forest,pk=forest_id)
    serializer = CommunitySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(forest=forest, user=user)
        communitys = forest.communitys.all()
        serializer = CommunitySerializer(communitys, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['PUT', 'DELETE'])
def community_update_or_delete(request, forest_id, community_pk):
    forest = get_object_or_404(Forest, pk=forest_id)
    community = get_object_or_404(Community, pk=community_pk)

    def update_community():
        if request.user == community.user:
            serializer = CommunitySerializer(instance=community, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                communitys = forest.communitys.all()
                serializer = CommunitySerializer(communitys, many=True)
                return Response(serializer.data)

    def delete_community():
        if request.user == community.user:
            community.delete()
            communitys = forest.communitys.all()
            serializer = CommunitySerializer(communitys, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_community()
    elif request.method == 'DELETE':
        return delete_community()



