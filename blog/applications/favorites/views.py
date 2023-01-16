from django.shortcuts import render
#
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import (
    View,
    ListView,
    DeleteView,
)
#
from applications.entrance.models import Entry
# models
from .models import Favorites


class UserPageView(LoginRequiredMixin, ListView):
    template_name = 'favorites/profile.html'
    context_object_name = 'entries_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entries_user(self.request.user)


class AddFavoritesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        user = self.request.user
        entry = Entry.objects.get(id=self.kwargs['pk'])
        # registramos favorito
        Favorites.objects.create(
            user=user,
            entry=entry,
        )

        return HttpResponseRedirect(
            reverse(
                'favorites_app:profile',
            )
        )


class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorites_app:profile')
