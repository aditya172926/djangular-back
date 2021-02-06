from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from myproject.api.serializers import UserSerializer
from rest_framework.authtoken.models import Token
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@csrf_exempt
def userLogout(request):
    dictionary = json.loads(request.body)
    tokenKey = dictionary['key']
    Token.objects.get(key = tokenKey).delete()
    return HttpResponse('Done')