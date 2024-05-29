from django.shortcuts import render
from rest_framework import viewsets

from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilistateurs connectes et authentifiés

    """
    # queryset = User.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "head", "patch", "delete"]
