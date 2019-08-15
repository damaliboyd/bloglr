from rest_framework import serializers
from api.models import Profile, Post, Comment

class ProfileSerializers(serializers.ModelSerializers):
    class Meta:
        model = Profile
        fields = ['__all__']
        read_only_fields = ['user']

class CommentSerializers(serializers.ModelSerializers):
    class Meta:
        model: Comment
        fields = ['text', 'author']
        read_only_fields = ['created']


class PostSerializers(serializers.ModelSerializers):
    comments = CommentSerializers(many=True)

    class Meta:
        model = Post
        fields = ['title','text']
        read_only_fields = ['created','modified']

    def create(self,validated_data):
        comments_data = validated_data.pop('comments')
        post = Post.objects.create(**validated_data)

        for comment_data in comments_data:
            Post.objects.create(post=post, **comment_data)
        return post
