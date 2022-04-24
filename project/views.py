from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import reverse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from .forms import CommentForm
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    queryset = Project.published.all()


class ProjectDetailView(View):

    def get(self, request, *args, **kwargs):
        view = ProjectDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProjectComment.as_view()
        return view(request, *args, **kwargs)


class ProjectDisplay(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class ProjectComment(SingleObjectMixin, FormView):
    model = Project
    form_class = CommentForm
    template_name = 'project/project_detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ProjectComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.project = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "A comment has been sent.")
        return reverse('project:project_detail', kwargs={'year': self.object.created_on.year,
                                                         'month': self.object.created_on.month,
                                                         'day': self.object.created_on.day,
                                                         'slug': self.object.slug}) + '#comments'
