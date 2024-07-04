import markdown # type: ignore
from django.shortcuts import render # type: ignore
from django.urls import reverse # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.contrib import messages # type: ignore
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
            messages.warning(request,"Error!")
            
        print(url_path)
        
        if url_path:
            return HttpResponseRedirect(url_path)
        
    
    if request.method == 'GET':    
        return render(request, "encyclopedia/index.html", {
            "files": util.list_entries()
        })

def titles(request, title):
    file = util.get_entry(title)
     
    if file is None:
        messages.warning(request, "Search Not found!")
        files = util.list_entries
        return render(request, "encyclopedia/search_results.html",{
            "files": files,          
        })        
    
    if request.method == "GET":
        html_convert = markdown.markdown(file)
        
        return render(request, "encyclopedia/titles.html", {
            "content": html_convert,
            "titles" : title
        })      

def new_page(request, titles: str | None=None, contents: str|None=None, message = None):  
  
    if request.method == "GET":
        try:
            return render(request, "encyclopedia/new_pg.html",{
                "titles": None,
                "contens": None,
                "message":None,
            })
        except Exception as z:
            messages.warning(request,f"ERROR! TRY AGAIN..{z}")
            
            
    if request.method == "POST":
       try:           
            title = request.POST.get("formGroupExampleInput", None)
            content = request.POST.get("FormControlTextarea1", None)               
                     
            if title:
                file = util.list_entries()
                if title in file:
                    messages.warning(request, f'This Title "{title}" Already Exists!')
                    return render(request, "encyclopedia/new_pg.html", {
                        "title": title,
                        "content": content,
                    }) 
            elif not content:
                messages.warning(request, f'Insert Contente for Coninue Save!')
                return render(request, "encyclopedia/new_pg.html", {
                    "title": title,
                    "content": content,
                })
            elif not title or not content:
                    messages.warning(request, "Insert Title and Content! Before Save!")
                    return render(request, "encyclopedia/new_pg.html", {
                        "title": title,
                        "content": content,
                    })        
                    
            try:
                util.save_entry(title,content)
                url_path = reverse("encyclopedia:titles", kwargs={"title": title})
                return HttpResponseRedirect(url_path)
                
            except Exception as z:
                messages.warning(f'ERROR! TRY AGAIN... {z}')
                        
       except Exception as z:
           messages.warning(f"FORM ERROR! TRY AGAIN...\n")
    
            
            


            