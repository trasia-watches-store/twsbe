from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'last_login', 'is_staff', 'date_joined')
        read_only_fields = ('last_login', 'date_joined')
        extra_kwargs = {
            'email': {'read_only': True}
        }