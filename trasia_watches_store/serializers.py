from rest_framework import serializers
from .models import Watch, WatchesPicture, MyModel

#################################################################################
class MyModelSerializer(serializers.ModelSerializer):

    # creator = serializers.ReadOnlyField(source='creator.username')
    # creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = MyModel
        fields = ['id', 'title', 'description', 'image_url']
#################################################################################
class WatchSerializer(serializers.ModelSerializer):
    wimage = serializers.ImageField(required=False)
    class Meta:
        model = Watch
        # fields = '__all__'
        fields = ('pk', 'name', 'type', 'wimage', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class WatchesPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchesPicture
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')