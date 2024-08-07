from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Bulletins, Responses


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletins
        fields = [
            'title',
            'category',
            'text',

        ]
        widgets = {
            'content': forms.CharField(widget=CKEditorWidget()),
        }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['respbulletins', 'text']
        widgets = {
          'text': forms.Textarea(attrs={'rows': 4, 'cols': 70}),
        }
