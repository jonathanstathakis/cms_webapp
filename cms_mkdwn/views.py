from django.views import generic

from cms_mkdwn.models import MarkdownContent

# Create your views here.


class MarkdownContentView(generic.DetailView):
    model = MarkdownContent
    template_name = "content.html"


class ContentListView(generic.ListView):
    model = MarkdownContent
    template_name = "content_list.html"
    context_object_name = "content_list"
