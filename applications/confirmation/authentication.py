from rest_framework.permissions import BasePermission

from applications.confirmation import models
from rest_framework import authentication, exceptions
from django.utils.translation import gettext_lazy as _


class TokenAuthentication(authentication.TokenAuthentication):
    model = models.Confirmation

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.get(slug=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return token, token


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return isinstance(request.user, models.Confirmation)
