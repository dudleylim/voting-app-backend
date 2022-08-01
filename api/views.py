from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
@api_view(['POST'])
def createUser(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username, '', password)
        user.save()
        return Response('user created')