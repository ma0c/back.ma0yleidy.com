from rest_framework import viewsets, mixins as viewsets_mixins

from applications.confirmation import serializers

class ConfirmationViewSet(
    viewsets_mixins.RetrieveModelMixin,
    viewsets_mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = serializers.ConfirmationSerializer
    queryset = serializers.ConfirmationSerializer.Meta.model.objects.all()
    lookup_field = 'slug'