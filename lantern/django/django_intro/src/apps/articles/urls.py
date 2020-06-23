from django.urls import path

from apps.articles.views import (
    SearchResultsView,
    ArticleListView,
    articles_json,
    ArticleFormView,
    index,
    main_page_logged_id,
)

app_name = "articles"

urlpatterns = [
    path("", index, name="index"),
    path("search/", main_page_logged_id, name="main-page"),
    path("results/", SearchResultsView.as_view(), name="search-results"),
    path("json/", articles_json, name="json-article-list"),
    path("list/", ArticleListView.as_view(), name="article-list"),
    path("form/", ArticleFormView.as_view(), name="article-form"),
]
