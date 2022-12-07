from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    if request.method=="POST":
        word=request.POST.get("word")

        return redirect("word-detail",word)
    return render(request,"swagger-ui.html")