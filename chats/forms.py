from django import forms
from .models import FileMessage


class ResumeForm(forms.ModelForm):
    class Meta:
        model = FileMessage
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.docx,.xls,.pdf,.png,.jpg'})
        }
