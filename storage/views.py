from django.shortcuts import render, redirect
from .models import Storage
from .forms import StorageForm
from django.views.generic import ListView


def home(req):
    return render(req, 'index.html')


# links
def links(request):
    links = Storage.objects.all()
    return render(request, 'links.html', {'links': links})


# add link
def add_link(req):
    form = StorageForm()
    if req.method == 'POST':
        form = StorageForm(req.POST)

        if form.is_valid():
            # form.save()
            instance = form.save(commit=False)
            instance.author = req.user
            instance.save()
            return redirect('/storage/')
    return render(req, 'add_link.html', {'form': form})


# update link
def update_link(request, pk):
    link = Storage.objects.get(id=pk)
    updateForm = StorageForm(instance=link)
    if request.method == 'POST':
        updateForm = StorageForm(request.POST, instance=link)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('/storage/')
    return render(request, 'edit_link.html', {'link': link, 'updateForm': updateForm})


# delete link
def delete_link(req, pk):
    link = Storage.objects.get(id=pk)
    link.delete()
    return redirect('/')
