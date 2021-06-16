from django.shortcuts import render, redirect, get_object_or_404
from .models import Storage
from .forms import StorageForm


def home(req):
    return render(req, 'index.html')


# links
def links(request):
    links = Storage.objects.all()
    is_favorite = False
    # test = Storage.favorite.filter(user_id=request.user.id).exists()
    for link in links:
        favorite = link.favorite.all()
        if favorite:
            is_favorite = True
    return render(request, 'links.html', {'links': links, 'is_favorite': is_favorite})


# add link
def add_link(req):
    form = StorageForm()
    if req.method == 'POST':
        form = StorageForm(req.POST, req.FILES)

        if form.is_valid():
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
        updateForm = StorageForm(request.POST, request.FILES, instance=link)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('/storage/')
    return render(request, 'edit_link.html', {'link': link, 'updateForm': updateForm})


# delete link
def delete_link(req, pk):
    link = Storage.objects.get(id=pk)
    link.delete()
    return redirect('/storage/')


# favorite
def favorite(request, pk):
    link = get_object_or_404(Storage, id=pk)
    # link = Storage.objects.get(id=pk)
    if link.favorite.filter(id=request.user.id).exists():
        link.favorite.remove(request.user)
    else:
        link.favorite.add(request.user)
    return redirect('/storage/')


def all_favorites(request):
    user = request.user
    favorites = user.favorite.all()
    return render(request, 'favorites.html', {'favorites': favorites})
