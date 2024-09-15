from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, QueryDict,HttpRequest
from django.urls import reverse, reverse_lazy
# from django.utils.text import slugify
from django.views.generic import (TemplateView, ListView, FormView, UpdateView,
                                  DetailView, DeleteView, CreateView)
from .forms import Form, PostForm
from .models import BlogPost, ThemePost
from pytils.translit import slugify

# from .sql_query import count_themes


class Themes:
    def get_themes(self):
        return ThemePost.objects.all().values('theme')


class HomePage(FormView):
    template_name = 'mainblog/index.html'
    form_class = Form
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_address'] = self.request.path
        context['title'] = 'Главная'

        return context


class BlogPage(Themes, ListView):
    template_name = 'mainblog/blog.html'
    model = BlogPost
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_address'] = self.request.path
        context['title'] = 'Блог'
        context['theme_post'] = ThemePost.objects.all()
        return context


class PostDetail(DetailView):
    # slug_field = 'title'
    template_name = 'mainblog/detailpost.html'
    context_object_name = 'post'
    model = BlogPost


class PostUpdate(LoginRequiredMixin,UpdateView):
    model = BlogPost
    template_name = 'mainblog/updatepost.html'
    context_object_name = 'post'
    form_class = PostForm
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog')
    template_name = 'mainblog/updatepost.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    success_url = reverse_lazy('blog')
    template_name = 'mainblog/createpost.html'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.save()
        return super().form_valid(form)


class FaqPage(TemplateView):
    template_name = 'mainblog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_address'] = self.request.path
        context['title'] = 'Вопросы и ответы'
        return context


class FilterPost(Themes, ListView):
    template_name = 'mainblog/blog.html'
    model = BlogPost
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_address'] = self.request.path
        context['title'] = 'Блог'
        context['theme_post'] = ThemePost.objects.all()

        if not self.request.GET.getlist('theme'):
            context['error_empty_list'] = 'Выберите тему'
            return context

        context['paginate_theme'] = self.request.GET.getlist('theme')
        return context

    def get_queryset(self):
        queryset = BlogPost.objects.filter(themes__slug__in=self.request.GET.getlist('theme'))
        if not queryset:
            return BlogPost.objects.all()
        return queryset