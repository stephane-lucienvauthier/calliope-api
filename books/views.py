"""This module manages the views of the categories app."""
from django.contrib.auth.models import Group
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Tag
from .serializers import BookUpdateSerializer, TagUpdateSerializer


class BooksView(APIView):
    """
    This class manages the view to create and list the products.
    Attributes:
        permission_classes (list(Permissions)): The options to access at this resource. 
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        """
        Create a book.

        Attributes:
            request (Request): The request sent to the api.
            format (NoneType): Always none, pass by Accept header.

        Returns:
            201: The book is created.
            400: An error is detected on the request data.
            401: The user must be connected to access this resource.
            406: The response format is not acceptable by the server.
            500: An error was occured in the treatment of the request.
        """
        tags = request.data['tags']
        tag_list = []
        for tag in tags:
            existing_tag = list(Tag.objects.filter(  # pylint: disable=no-member
                value=tag['value']).values())
            if not existing_tag:
                tag_serializer = TagUpdateSerializer(data=tag)
                if tag_serializer.is_valid():
                    tag_serializer.save()
                    tag_list.append(tag_serializer.data['id'])
            else:
                tag_list.append(existing_tag[0]['id'])

        request.data['tags'] = tag_list
        serializer = BookUpdateSerializer(data=request.data)
        if serializer.is_valid():
            group = Group.objects.get(name=list(request.user.groups.filter(
                name__startswith='cp_'))[0].name)
            serializer.save(owner=group)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
