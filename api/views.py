from django.shortcuts import render

# Create your views here.
def api(requete):
    return render(requete,'index.html',{})