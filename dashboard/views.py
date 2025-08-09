from django.shortcuts import render
from .forms import NotesForm
from .models import Notes
from django.contrib import messages

def home(request):
    return render(request,'dashboard/home.html')

from django.shortcuts import render, redirect
from .forms import NotesForm
from .models import Notes
from django.contrib import messages

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = Notes(
                user=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description']
            )
            note.save()
            messages.success(request, f"Notes added from {request.user.username} successfully") 
        
        
        return redirect('notes')  # 'notes' is the URL name for this view
    
    
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)


def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")
