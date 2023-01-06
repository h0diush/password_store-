from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DeleteView


class DeleteViewMixin(LoginRequiredMixin, DeleteView):
    """Mixin для удаления модели паролей"""

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
