from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Document
from .forms import DocumentForm


def index(request):
    documents = Document.objects.all()
    context = {
        'documents': documents,
    }
    return render(request, 'documents/index.html', context)
    

def search(request):
    query = request.GET.get('q')
    # documents = Document.objects.filter(
    #                           Q(markdown__icontains=query)
    #                       )
    documents = Document.search_in_markdown(query)
    context = {
        'query': query,
        'documents': documents,
    }
    return render(request, 'documents/search.html', context)

def new(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            return redirect('documents:index')
    else:
      form = DocumentForm()
    context = {
        'form': form,
    }
    return render(request, 'documents/new.html', context)
