from django import forms
from .models import DocxModel


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocxModel
        fields = ('description', 'work_shift', 'number_check', 'document')