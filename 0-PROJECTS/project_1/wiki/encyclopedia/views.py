from django.http import Http404
import markdown
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from . import util


def index(request):    
    if request.method == "POST":
        
        q = request.POST.get("q", None)
        print(request.POST)
        print(q)
        
        url_path = None
        try:
            url_path = reverse("encyclopedia:titles", kwargs={"title": q})
        except Exception as z:
            print(z)
            
        print(url_path)
        
        if url_path:
            return HttpResponseRedirect(url_path)
        
    
    if request.method == 'GET':    
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def titles(request, title):
    file = util.get_entry(title)
     
    if file is None:
        message = messages.warning(request, "Search Not found!")
        files = util.list_entries
        return render(request, "encyclopedia/search_results.html",{
            "entries": files, 
            "message": message,           
        })        
    
    if request.method == "GET":
        html_convert = markdown.markdown(file)
        
        return render(request, "encyclopedia/titles.html", {
            "content": html_convert,
            "titles" : title
        })       
