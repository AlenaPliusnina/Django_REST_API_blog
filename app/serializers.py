from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Post, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):

    author_id = serializers.IntegerField(source="author.id")
    author_username = serializers.CharField(read_only=True, source="author.username")

    def create(self, validated_data):
        author_id = validated_data.pop("author", {}).pop("id", None)

        if not author_id:
            raise Exception("Incorrect author id")

        try:
            author = User.objects.get(id=author_id)
        except User.DoesNotExist:
            raise Exception("Author Does Not Exist")
        return Post.objects.create(author=author, **validated_data)

    class Meta:
        model = Post
        fields = ['id', 'title', 'status', 'content', 'updated', 'publication_date', 'author_id',
                  'author_username', 'category']


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Account
#         fields = ['url', 'id', 'account_name', 'users', 'created']
