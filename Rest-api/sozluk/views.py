from django.shortcuts import render, redirect


def home(request):
    if request.method == "POST":
        word: str = str(request.POST.get("word")).lstrip().strip().lower()

        return redirect("word-detail", word)
    return render(request, "swagger-ui.html")
