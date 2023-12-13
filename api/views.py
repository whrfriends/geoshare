from django.shortcuts import render

# Create your views here.
def api(requeste):
    return render(requeste,'index.html',{})
