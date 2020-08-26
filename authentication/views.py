"""This module manages the views of the authentication app."""
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response


class LoginView(ObtainAuthToken):
    """This class manages the view for the login resources."""

    def post(self, request: Request, *args: tuple, **kwargs: dict):
        """
        Log in a user.

        Args:
            request (Request): The api request.
            args (tuple): The key list of arguments.
            kwargs (dict): The value list of arguments.

        Returns:
            201: The user is logged.
            400: An error is detected on the request data.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)  # pylint: disable=no-member
        return Response({
            'token': token.key,
            'email': user.email,
            'created': created,
            'permissions': user.get_all_permissions()
        })
