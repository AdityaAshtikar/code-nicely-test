from django import forms
from notes.models import Note
from django.core.validators import RegexValidator, MinLengthValidator


class NoteForm(forms.Form):
    title = forms.CharField(max_length=50,
                            required=True, label="Title", validators=[MinLengthValidator(5)])
    text = forms.CharField(max_length=500, label="Text", required=True,
                           validators=[MinLengthValidator(10)], widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    class Meta:
        model = Note
        fields = ['title', 'text']
