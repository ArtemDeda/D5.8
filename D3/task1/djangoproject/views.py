from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from .filters import NewsFilter
from .models import News
from .forms import NewsForm, CategoryForm


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 10
    ordering = ['-date_published']


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


def news_list(request):
    news = News.objects.all().order_by('-date_published')
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})


def index(request):
    return render(request, 'index.html')


def news_search(request):
    news_list = News.objects.all()
    news_filter = NewsFilter(request.GET, queryset=news_list)
    return render(request, 'news/search.html', {'filter': news_filter, 'date_published': News.date_published})


@login_required(login_url='/403/')
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/create.html', {'form': form})


def error_403(request):
    return render(request, 'error_403.html')


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('djangoproject.add_product',)
    raise_exception = True
    form_class = NewsForm
    model = News
    template_name = 'news/create.html'
    success_url = reverse_lazy('news_list')


def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list', pk=pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/edit_news.html', {'form': form})


def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'news/delete_news.html', {'news': news})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = CategoryForm()
    return render(request, 'news/create_category.html', {'form': form})


def yandex_login(request):
    if request.method == 'GET':
        return redirect(f"https://oauth.yandex.ru/authorize?response_type=code&client_id={settings.YANDEX_CLIENT_ID}")
    elif request.method == 'POST':
        pass
