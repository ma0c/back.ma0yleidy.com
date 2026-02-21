from rest_framework import serializers

from applications.confirmation.models import Confirmation

class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmation
        fields = (
            'is_confirmed',
            'minutes'
        )