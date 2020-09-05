"""This module defines the models of the books app."""
from django.db import models
from django.contrib.auth.models import Group


class Tag(models.Model):
    """
    This class defines the tag model.

    Attributes:
        value (str): The tag value.
    """

    value = models.CharField(max_length=255)

    def __str__(self):
        """Return the value when the model is called directly."""
        return self.value

    class Meta:
        """
        This class defines metadata for the model.

        Attributes:
            ordering (list(str)): The list to sort a list of models.
        """

        ordering = ['value']


class Book(models.Model):
    """
    This class defines the book model.
    Attributes:
        owner (Group): The book owner.
        title (str): the book title.
        isbn (str):  The book identifier.
        parution (int): The year of the first parution.
        description (str): The book description.
        cover (str): The book cover.
        tags (List(Tag)): The book tags.
    """

    owner = models.ForeignKey(Group, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    parution = models.IntegerField(default=2020)
    description = models.TextField(null=True)
    cover = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        """Return the value when the model is called directly."""
        return self.title

    class Meta:
        """
        This class defines metadata for the model.
        Attributes:
            ordering (list(str)): The list to sort a list of models.
        """

        ordering = ['title']
