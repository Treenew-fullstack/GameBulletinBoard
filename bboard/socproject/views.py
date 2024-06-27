from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bulletins, Responses
from .forms import BulletinForm, ResponseForm
from .filters import ResponsesFilter


class BulletinsListView(ListView):
    model = Bulletins
    template_name = 'bulletins.html'
    context_object_name = 'bulletins'
    ordering = ['title']


class BulletinDetailView(DetailView):
    model = ResponseForm
    template_name = 'bulletindetail.html'
    context_object_name = 'bulletin'


class BulletinCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bulletincreate.html'
    form_class = BulletinForm


class BulletinEditView(LoginRequiredMixin, UpdateView):
    form_class = BulletinForm
    model = Bulletins
    template_name = 'bulletinedit.html'


class BulletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulletins
    template_name = 'bulletindelete.html'
    success_url = reverse_lazy('socproject:bulletins')


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


def acceptresponse(*args, **kwargs):
    reply = Responses.objects.get(id=kwargs.get('pk'))
    reply.accepted = True
    reply.save()
    #notify_accept_reply(reply.id)
    return redirect('socproject:showresponses')

def rejectresponse(*args, **kwargs):
    response = Responses.objects.get(id=kwargs.get('pk'))
    response.delete()
    return redirect('socproject:showresponses')


