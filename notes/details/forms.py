from django import forms
from details.models import Note

class NoteCreateForm(forms.ModelForm):
    class Meta:
        fields = ("title",'content')
        model = Note