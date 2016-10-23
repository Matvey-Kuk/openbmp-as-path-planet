from rest_framework import serializers
from rest.models import PathUpdate, AS, Prefix


class ASSerializer(serializers.ModelSerializer):
    class Meta:
        model = AS
        fields = ('id', 'number', 'latitude', 'longitude')


class PrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefix
        fields = ('id', 'prefix')


class PathUpdateSerializer(serializers.ModelSerializer):
    paths = ASSerializer(many=True, read_only=True)
    prefix = PrefixSerializer(read_only=True)

    class Meta:
        model = PathUpdate
        fields = ('id', 'time', 'prefix', 'paths', 'peer')
