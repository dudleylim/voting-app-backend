from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import CandidateSerializer, VoteSerializer
from .models import Candidate, Vote

# Create your views here.
@api_view(['POST'])
def createUser(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username, '', password)
        user.save()
        return Response('user created')

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def requestVotes(request):
    if request.method == 'GET':
        user = request.user
        votes = user.vote_set.all()
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(print(serializer))

    if request.method == 'DELETE':
        pk = request.data['id']
        vote = Vote.objects.get(id=pk)
        vote.delete()
        return Response('Vote deleted')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def requestVotesAll(request):
    if request.method == 'GET':
        votes = Vote.objects.all()
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def requestCandidates(request):
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)