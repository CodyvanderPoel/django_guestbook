from django import forms


class NoteForm(forms.Form):
    name = forms.CharField(label="Your Name:")
    date = forms.DateField()
    note = forms.CharField(label="Your Note:")
