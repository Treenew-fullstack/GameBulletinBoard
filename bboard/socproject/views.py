from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bulletins, Responses
from .forms import BulletinForm


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


class BulletinEditView(LoginRequiredMixin, UpdateView):
    form_class = BulletinForm
    model = Bulletins
    template_name = 'bulletinedit.html'


class BulletinDeleteView(LoginRequiredMixin, DeleteView):
    model = Bulletins
    template_name = 'bulletindelete.html'
    success_url = reverse_lazy('bulletins')

