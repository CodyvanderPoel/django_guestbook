from django.shortcuts import render
from django.views import View
from app import forms

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Note(View):
    def get(self, request):
        return render(request, 'note.html', {'NoteForm': forms.NoteForm()})

    def post(self, request):
        form = forms.NoteForm(data=request.POST)
        if form.is_valid():
            name, date, note = form.cleaned_data['name'], form.cleaned_data[
                'date'], form.cleaned_data['note']
            return render(request, 'note.html')
