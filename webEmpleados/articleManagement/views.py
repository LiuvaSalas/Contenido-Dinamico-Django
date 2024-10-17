from django.shortcuts import render
from articleManagement.models import Article
from articleManagement.forms import FormularioArticle


# Create your views here.
def article(request):
    articulo = request.GET["articulo"]
    articulos = Article.objects.filter(name__icontains=articulo)
    return render(request, "article.html", {"articulos": articulos, "query": articulo})


def create_article(request):
    form = FormularioArticle()
    if request.method == "POST":
        form = FormularioArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "create_article.html", {"form": form})
