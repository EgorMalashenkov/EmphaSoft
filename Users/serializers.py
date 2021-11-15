from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        user = get_user_model()
        model = user
        fields = ('username', 'first_name', 'last_name', 'last_login', 'email')
