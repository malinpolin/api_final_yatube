from django.shortcuts import get_object_or_404

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

from api.mixins import BaseFollowViewSet, BasePostCommentViewSet


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
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


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
    search_fields = ('=following__username', )

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
