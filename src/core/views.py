import pathlib

from django.http import HttpResponse
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    title = "Home Page"
    context = {
        "title": title,
    }
    html_template = "home.html"
    return render(request, html_template,context=context)


def about_page_view(request, *args, **kwargs):
    title = "Home Page"
    context = {
        "title": title,
    }
    html_template = "home.html"
    return render(request, html_template,context=context)