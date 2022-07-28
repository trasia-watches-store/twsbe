from rest_framework import serializers
from .models import Watch, WatchesPicture

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        # fields = '__all__'
        fields = ('pk', 'name', 'type', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class WatchesPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchesPicture
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')