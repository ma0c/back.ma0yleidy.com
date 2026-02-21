from applications.confirmation import authentication

class IsAuthenticatedAppMixin:
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [authentication.IsAuthenticated]