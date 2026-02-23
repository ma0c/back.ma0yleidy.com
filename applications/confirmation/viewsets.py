from rest_framework import viewsets, mixins as viewsets_mixins

from applications.confirmation import serializers
from rest_framework.response import Response

class ConfirmationViewSet(
    viewsets_mixins.RetrieveModelMixin,
    viewsets_mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = serializers.ConfirmationSerializer
    queryset = serializers.ConfirmationSerializer.Meta.model.objects.all()
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print("Request data:")
        print(request.data)
        print("=================================")
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)