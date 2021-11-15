from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserModelSerializer


# if the user wants to update/delete his data, then we needs to use djoser endpoints


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.filter(is_staff=False)

    def get_permissions(self):
        if self.action in ('list', 'update', 'partial_update', 'destroy', 'create'):
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
