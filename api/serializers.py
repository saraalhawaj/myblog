from django_comments.models import Comment
from rest_framework import serializers
from posts.models import Post

class PostListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api:detail",
		lookup_field = "slug",
		lookup_url_kwarg = "post_slug"
		)
	class Meta:
		model = Post
		fields = ['title', 'author', 'publish_date', 'detail']

class PostDetailSerializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField()
	full_name = serializers.SerializerMethodField()
	comments = serializers.SerializerMethodField()

	class Meta:
		model = Post
		fields = "__all__"

	def get_user(self, obj):
		return str(obj.author.username)

	def get_full_name(self, obj):
		return "%s %s" % (obj.author.first_name, obj.author.last_name)

	def get_comments(self, obj):
		comment_queryset = Comment.objects.filter(object_pk=obj.id)
		comments = CommentListSerializer(comment_queryset, many=True).data
		return comments

class PostCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'content', 'publish_date', 'draft', 'img']


class CommentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['content_type', 'object_pk','user','comment','submit_date']

class CommentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['object_pk','comment']