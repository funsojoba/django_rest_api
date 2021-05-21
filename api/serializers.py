from rest_framework import serializers
from bookapp.models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'subtitle', 'author', 'isbn')