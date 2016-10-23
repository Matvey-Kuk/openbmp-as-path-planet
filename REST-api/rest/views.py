import json

from rest_framework import viewsets
from rest_framework.response import Response

from rest.models import PathUpdate, AS, Prefix
from rest.serializers import PathUpdateSerializer, ASSerializer, PrefixSerializer
from django.db.models import Count


class ASListViewSet(viewsets.ModelViewSet):
    serializer_class = ASSerializer
    queryset = AS.objects.all()


class PrefixViewSet(viewsets.ModelViewSet):
    serializer_class = PrefixSerializer
    queryset = Prefix.objects.all()


class UpdatesListViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    serializer_class = PathUpdateSerializer
    queryset = PathUpdate.objects.all()

    def list(self, request):
        as_paths = []

        try:
            as_paths = json.JSONDecoder().decode(request.GET.get('as_paths', ''))
        except:
            print("No as paths in request")

        prefixes = []
        try:
            prefixes = json.JSONDecoder().decode(request.GET.get('prefixes', ''))
        except:
            print("No prefixes in request")

        print (prefixes)

        updates = PathUpdate.objects.all()

        if len(prefixes) > 0:
            updates = updates.filter(prefix__prefix__in=prefixes)

        if len(as_paths) > 0:
            updates = updates.filter(paths__number__in=as_paths)

        serializer = self.get_serializer(updates, many=True)
        return Response(serializer.data)
