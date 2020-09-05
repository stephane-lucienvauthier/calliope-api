"""This module defines the serializers for the books app."""
from rest_framework import serializers
from .models import Book, Tag


class TagUpdateSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the tags view."""

    class Meta:
        """
         This class defines the validation metadata for the tags view.

        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Tag
        fields = ['id', 'value']


class BookUpdateSerializer(serializers.ModelSerializer):
    """This class defines the serializer for the books view."""

    class Meta:
        """
         This class defines the validation metadata for the books view.

        Attributes:
            model (Model): The model linked to the serializer.
            fields (list(str)): The field list expencted by the serializer.
        """

        model = Book
        fields = ['id', 'title', 'isbn', 'parution',
                  'description', 'cover', 'tags']
