from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class Index(TemplateView):
    template_name = 'index.html'
