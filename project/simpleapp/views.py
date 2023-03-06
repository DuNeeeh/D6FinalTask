from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .filters import NewsFilter
from .forms import NewsForm, PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class NewsList(ListView):
    model = News
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class NewsSearchList(ListView):
    model = News
    ordering = '-dateCreation'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add.news',)
    raise_exception = True
    form_class = NewsForm
    model = News
    template_name = 'news_create.html'


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_news',)
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')
