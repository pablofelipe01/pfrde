from rest_framework import serializers
from .models import Pferd


class PferdSerializer(serializers.HyperlinkedModelSerializer):
    pferd_url = serializers.ModelSerializer.serializer_url_field(
        view_name="pferd_detail")

    class Meta:
        model = Pferd
        fields = ('id', 'name', 'line', 'breed',
                  'img_url', 'video_url', 'pferd_url')
