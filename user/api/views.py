from rest_framework import generics
from ..models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework import viewsets
from django.http import HttpResponse


class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        serializer_class = UserSerializer(request.user)
        return Response(serializer_class.data)

    @classmethod
    def get_extra_actions(cls):
        return []


def my_view(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(request, username=username, password=password)
    if user == None:
        return HttpResponse("Авторизация не прошла")
    login(request, user)
    return HttpResponse("Авторизация прошла успешно")





