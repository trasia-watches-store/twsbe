from rest_framework import serializers
from .models import Watch  

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        # fields = '__all__'
        fields = ('pk', 'name', 'type', 'image', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'image': {'read_only': True}
        }