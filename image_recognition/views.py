from django.shortcuts import render
from django.http import HttpResponse



def check_image(request, id):
    print("id",id)
    context = {'id':id,'name':'shikha'}
    return render(request, "profile_page.html", context=context)

# Create your views here.
