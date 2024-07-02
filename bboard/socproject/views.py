from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bulletins, Responses
from .forms import BulletinForm, ResponseForm
from .filters import ResponsesFilter
from .tasks import create_new_response, accept_response_message


class BulletinsListView(ListView):
    model = Bulletins
    template_name = 'bulletins.html'
    context_object_name = 'bulletins'
    ordering = ['title']


class BulletinDetailView(DetailView):
    model = Bulletins
    template_name = 'bulletindetail.html'
    context_object_name = 'bulletin'


class BulletinCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bulletincreate.html'
    form_class = BulletinForm

    def form_valid(self, form):
        bulletin = form.save(commit=False)
        bulletin.author = User.objects.get(id=self.request.user.id)
        bulletin.save()
        return redirect('socproject:bulletins')


class BulletinEditView(LoginRequiredMixin, UpdateView):
    form_class = BulletinForm
    model = Bulletins
    template_name = 'bulletinedit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bulletin_author'] = Bulletins.objects.get(pk=self.kwargs.get('pk')).author
        return context


class BulletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulletins
    template_name = 'bulletindelete.html'
    success_url = reverse_lazy('socproject:bulletins')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bulletin_author'] = Bulletins.objects.get(pk=self.kwargs.get('pk')).author
        return context


class ResponsesListView(LoginRequiredMixin, ListView):
    model = Responses
    template_name = 'showresponses.html'
    context_object_name = 'response'

    def get_queryset(self):
        queryset = Responses.objects.filter(respbulletins_id__author_id=self.request.user.id)
        self.filterset = ResponsesFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Responses.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class ResponseCreateView(LoginRequiredMixin, CreateView):
    model = Responses
    form_class = ResponseForm
    template_name = 'responsecreate.html'
    context_object_name = 'respcreate'

    def form_valid(self, form):
        response = form.save(commit=False)
        response.author = User.objects.get(id=self.request.user.id)
        response.respbulletins = Bulletins.objects.get(id=self.kwargs.get('pk'))
        response.save()
        create_new_response(response.id)
        return redirect('socproject:bulletins')


def acceptresponse(*args, **kwargs):
    response = Responses.objects.get(id=kwargs.get('pk'))
    response.status = True
    response.save()
    accept_response_message(response.id)
    return redirect('socproject:showresponses')


def rejectresponse(*args, **kwargs):
    response = Responses.objects.get(id=kwargs.get('pk'))
    response.status = False
    response.save()
    return redirect('socproject:showresponses')
