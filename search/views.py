from django.shortcuts import render, redirect
from storage.models import Storage


def search(request):
    search_query = request.GET.get('search')
    if not search_query:
        search_query = ""
    links = Storage.objects.filter(title__icontains=search_query)
    # return redirect('search/', {'links': links})
    return render(request, 'search/search_result.html',  {'links': links})

# def search_result(request):
#     # return redirect('search/')
#     return render(request, 'search/search_result.html',  {'links': links})


def search_bar(request):
    # return redirect('search/')
    return render(request, 'search/search_bar.html')
