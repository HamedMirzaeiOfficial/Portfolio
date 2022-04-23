from django.http import HttpResponseForbidden
from django.shortcuts import reverse
from .models import Post
from django.views.generic import ListView, DetailView, TemplateView, FormView, View
from .forms import CommentForm
from django.views.generic.detail import SingleObjectMixin


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.published.all()


class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


class PostDisplay(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        # post = self.get_object()
        # return reverse('blog:post_detail', kwargs={'year': post.created_on.year,
        #                                            'month': post.created_on.month,
        #                                            'day': post.created_on.day,
        #                                            'slug': post.slug}) + '#comments'
        #

        return reverse('blog:post_detail', kwargs={'year': self.object.created_on.year,
                                                   'month': self.object.created_on.month,
                                                   'day': self.object.created_on.day,
                                                   'slug': self.object.slug}) + '#comments'


class HomeView(TemplateView):
    template_name = 'home.html'


class ResumeView(TemplateView):
    template_name = 'resume.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
