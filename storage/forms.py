from django import forms
from .models import Storage


class StorageForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'description', 'link_path',
                  'cover', 'cover_url', 'alt', 'category', 'private']
        model = Storage
