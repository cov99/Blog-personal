import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)
# apps entry
from applications.entrance.models import Entry
# models
from .models import Home
# forms
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home
        context["home"] = Home.objects.latest('created')
        # contexto de portada
        context["portada"] = Entry.objects.front_page_entry()
        # contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entries_in_home()
        # entradas recientes
        context["entradas_recientes"] = Entry.objects.entries_recent()
        # enviamos formulario de suscripcion
        context["form"] = SuscribersForm
        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'
