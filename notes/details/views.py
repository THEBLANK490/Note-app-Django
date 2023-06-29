from django.shortcuts import render, redirect
from details.models import Note
from details.forms import NoteCreateForm

# Create your views here.

def update(request, id):
    notes_obj = Note.objects.get(id =id)
    title = request.POST.get('title','')
    content = request.POST.get('content','')
    
    if request.method == 'POST':
        notes_obj.title = title
        notes_obj.content = content
        print(title)
        notes_obj.save()
        return redirect('update',id)
    context = {'data' : notes_obj,'id': id}
    return render(request, "details/update.html", context)


def details(request):
    id = int(request.GET.get('id',0))
    notes = Note.objects.all()

    if request.method == 'POST':
        id = int(request.POST.get('id',0))
        title =request.POST.get('title','')
        content = request.POST.get('content','')

        if id > 0:
            note = Note.objects.get(id = id)
            note.title = title
            note.content = content
            note.save()

            return redirect('/',id)
        else:
            note= Note.objects.create(title = title , content = content)
            return redirect('/' ,note.id)

 
    if id > 0:
        note = Note.objects.get(id = id)
    else:
        note = ''
    

    context = {
        'id':id,
        'notes':notes,
        'note' :note
    }
    return render(request, 'details/details.html',context)


def delete(request,id):
    note_obj = Note.objects.get(id = id)
    context = {'data':note_obj}
    note_obj.delete()
    return redirect('details')


