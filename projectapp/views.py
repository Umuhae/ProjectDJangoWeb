from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreateForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription, **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # Display only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        try:
            current_page = int(page) if page else 1
        except:
            current_page = 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = min(start_index + page_numbers_range, max_index)
        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context