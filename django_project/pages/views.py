from django.views.generic import TemplateView


# Create your views here.
class home_page_view(TemplateView):
    template_name = "home.html"

class about_page_view(TemplateView):
    template_name = "about.html"

class exp_page_view(TemplateView):
    template_name = "experience.html"

class proj_page_view(TemplateView):
    template_name = "projects.html"

class contact_page_view(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["LinkedIn"] = "Ruben's LinkedIn"
            context["email"] = "ruben.marrow@umontana.edu"
            context["github"] = "Ruben's GitHub"
            return context