from django.urls import path

from . import views

app_name = "cms_mkdwn"

urlpatterns = [
    path("", views.ContentListView.as_view(), name="home"),
    path("<int:pk>", views.MarkdownContentView.as_view(), name="content-detail"),
]
