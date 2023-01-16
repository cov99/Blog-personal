from django.shortcuts import render
#
from django.views.generic import (
    ListView,
    DetailView
)
# models
from .models import Entry, Category


class EntryListView(ListView):
    template_name = "entrance/list.html"
    context_object_name = 'entries'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        category = self.request.GET.get("category", '')
        # consulta de busqueda
        result = Entry.objects.search_entry(kword, category)
        return result


class EntryDetailView(DetailView):
    template_name = 'entrance/detail.html'
    model = Entry
