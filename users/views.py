from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import (
    User,
    UpgradeRequest
  )

from .serializers import (
    UserSerializer,
    UpgradeRequestSerializer,
    UpgradeRequestUserSerializer
  )


class UserViewSet(ModelViewSet):
    filter_fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'type']

    def get_queryset(self):
        queryset =  User.objects.all()
        return queryset

    def get_serializer_class(self):
        return UserSerializer

    @list_route(methods=['get'])
    def get_profile(self, request):
        try:
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response(e)


class UpgradeRequestViewSet(ModelViewSet):
    filter_fields = ['upgrade_request_related_user', 'first_name', 'last_name', 'gender']

    def get_queryset(self):
        queryset = UpgradeRequest.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request and self.request.user and self.request.user.is_superuser():
            return UpgradeRequestSerializer
        return UpgradeRequestUserSerializer

    def perform_create(self, serializer):
        serializer.save(upgrade_request_related_user=self.request.user)
