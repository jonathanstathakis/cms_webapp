from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "cms_webapp/home.html"
