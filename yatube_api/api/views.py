from django.shortcuts import get_object_or_404

from rest_framework import mixins as mx
from rest_framework import viewsets, permissions, filters

from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group

from api.serializers import (
    PostSerializer,
    CommentSerializer,
    GroupSerializer,
    FollowSerializer
)

from api.permissions import IsAuthorOrReadOnly


class BasePostCommentViewSet(
    mx.CreateModelMixin,
    mx.ListModelMixin,
    mx.RetrieveModelMixin,
    mx.DestroyModelMixin,
    mx.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """
    Этот базовый вьюсет предоставляет следующие действия:
    'list', 'create', 'retrieve', 'update', 'partial_update', 'destroy'.
    """
    pass


class BaseFollowViewSet(
    mx.CreateModelMixin,
    mx.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Этот базовый вьюсет предоставляет следующие действия:
    'list', 'create'.
    """
    pass


class PostViewSet(BasePostCommentViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(BasePostCommentViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Этот вьюсет предоставляет 'list' и 'retrieve' действия.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(BaseFollowViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
