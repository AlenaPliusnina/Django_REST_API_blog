from django.contrib.auth.models import User
from app.models import Post, Category
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'status', 'content', 'updated', 'publication_date', 'author', 'category']


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['url', 'id', 'account_name', 'users', 'created']
