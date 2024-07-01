from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from projects.models import Contributor
from rest_framework.decorators import action


class RecordInterestView(SingleObjectMixin, View):
    """Records the current user's interest in an author."""

    model = Contributor

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        # Look up the author we're interested in.
        self.object = self.get_object()
        # Actually record interest somehow here!

        return HttpResponseRedirect(
            reverse("author", kwargs={"pk": self.object.pk})
        )


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class GetDetailSerializerClassMixin:
    """
    Get detail serializer class
    """

    def get_serializer_class(self):
        if (
                self.action == "retrieve"
                or self.action == "create"
                or self.action == "update"
                and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()
