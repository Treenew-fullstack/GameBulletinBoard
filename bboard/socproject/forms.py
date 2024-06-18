from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives

from .models import Bulletins, Responses


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletins
        fields = [
            'author',
            'title',
            'category',
            'text',

        ]

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['text', ]
        widgets = {
          'text': forms.Textarea(attrs={'rows': 4, 'cols': 70}),
        }
