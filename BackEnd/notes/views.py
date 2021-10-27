from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import Artist, Note,Tag

from rest_framework.decorators import api_view

from rest_framework.response import Response

from django.http import Http404

from .serializers import NoteSerializer , ArtistSerializer


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_note = request.POST.get('tag')
        tag_list = Tag.objects.filter(name=tag_note)
        if len(tag_list)==0:
            tag=Tag(name=tag_note)
            tag.save()
        else:
            tag=tag_list[0]
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        b = Note(title=title, content=content,tag=tag)
        b.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
    
        return render(request, 'notes/index.html', {'notes': all_notes})


def edit(request):
    id = request.POST.get('id')
    ID=int(id)
    note= Note.objects.get(id=ID)
    if request.method == 'POST':
        title = request.POST.get('newtitle')
        content = request.POST.get('newdetails')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/index.html', {'notes': note})


# def delete(request):
#     id = request.POST.get('id')
#     ID=int(id)
#     note = Note.objects.get(id=ID)
#     p_tag=request.POST.get('tag')
#     if p_tag is not None:
#         tag = Note.objects.filter(tag=p_tag)
#         if len(tag)==0:
#             Tag.objects.filter(name=p_tag).delete()
#     note.delete()
#     return redirect('index')

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        Note.objects.filter(id=id).delete()

        if tag is not None:
            tag_list = Note.objects.filter(tag__name=tag)
            if len(tag_list) == 0:
                Tag.objects.filter(name=tag).delete()

        return redirect('index')
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes, 'tags':all_tags})

def list_of_tags(request):

    p_tag=request.POST.get('tag')

    t_tag=Tag.objects.get(id=p_tag)

    filtered_notes=Note.objects.filter(tag=t_tag)

    return render(request, 'notes/tags.html', {'notes': filtered_notes})

def all_tags(request):
    all_tags = Tag.objects.all()
    return render(request,'notes/alltags.html',{'tags': all_tags})

@api_view(['GET', 'POST'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()


    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)

@api_view(['GET','POST'])
def api_note_list(request):

    if request.method == "POST":
        new_note_data = request.data
        note = Note()
        note.title = new_note_data["title"]
        note.content = new_note_data["content"]
        note.save()
        
    notes= Note.objects.all()

    serialized_notes = NoteSerializer(notes,many=True)
    return Response(serialized_notes.data)

@api_view(['GET', 'POST'])
def api_artist(request, request_id):
    try:
        artist = Artist.objects.get(id=request_id)
    except Artist.DoesNotExist:
        raise Http404()

    # if request.method == 'POST':
    #     new_note_data = request.data
    #     note.title = new_note_data['title']
    #     note.content = new_note_data['content']
    #     note.save()
    serialized_artist = ArtistSerializer(artist)
    return Response(serialized_artist.data)

