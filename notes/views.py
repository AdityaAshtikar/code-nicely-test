from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Note, Shared
import json


@csrf_exempt
@login_required
def home(request):
    note = {}
    if request.method == 'POST':
        response_data = {}
        form = NoteForm(request.POST)
        data = Note(title=request.POST.get('title'),
                    text=request.POST.get('text'), author=request.user)
        data.save()
        messages.success(
            request, f'Added new Note: {request.POST.get("title")}.')
        response_data['text'] = request.POST.get('text')
        response_data['title'] = request.POST.get('title')
        response_data['created'] = data.created_date.strftime(
            '%B %d, %Y %I:%M %p')
        response_data['author'] = data.author.full_name
        note = response_data
    else:
        form = NoteForm()

    # pulling notes from db
    notes = Note.objects.all().filter(
        author=request.user.id).order_by('id').reverse()

    return render(request, 'home.html', {'form': form, 'notes': notes, 'note': note})
