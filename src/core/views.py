import pathlib

from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    # queryset = PageVisit.objects.all()
    queryset = PageVisit.objects.filter(path=request.path)

    title = "Home Page"
    context = {
        "title": title,
        "visit_count": queryset.count(),
    }
    PageVisit.objects.create(path=request.path)
    html_template = "home.html"
    return render(request, html_template,context=context)


def about_page_view(request, *args, **kwargs):
    title = "Home Page"
    context = {
        "title": title,
    }
    html_template = "home.html"
    return render(request, html_template,context=context)