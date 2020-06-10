from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, FormView, ListView

from apps.articles.forms import ArticleImageForm, ArticlesForm
from apps.articles.models import Article


def main_page(request, some_id=None, *args, **kwargs):
    return render(request, "pages/main_page.html")


@login_required
def main_page_logged_id(request, some_id=None, *args, **kwargs):
    return render(request, "pages/main_page.html")


class SearchResultsView(View):
    def get(self, request, **kwargs):
        search_q = request.GET.get("search", "")
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {"articles": articles}

        return render(request, "pages/search.html", context=context_data)

    def post(self, request):
        return HttpResponse("{}", status=201)


def articles_json(request):
    articles = Article.objects.all().values()
    list_of_articles = [article for article in articles]
    return JsonResponse(list_of_articles, safe=False)


class ArticleListView(ListView):
    model = Article
    template_name = "articles.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "article.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tits"] = 42
        return ctx


class ArticleUpdateImageView(FormView):
    form_class = ArticleImageForm
    template_name = "article_image-update.html"

    def get_success_url(self):
        return reverse("articles:detail", kwargs={"id": self.kwargs["id"]})

    def form_valid(self, form):
        # get_object_or_404()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["id"] = self.kwargs["id"]

        return ctx


class ArticleFormView(FormView):
    template_name = "articles_form.html"
    form_class = ArticlesForm
    success_url = "/articles/search/"
