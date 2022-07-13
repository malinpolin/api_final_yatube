from rest_framework import mixins as mx
from rest_framework import viewsets


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
