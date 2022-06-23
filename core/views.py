from django.views.generic import TemplateView  # Import do TemplateView para trabalhar com class based view
 
class indexView(TemplateView):
    template_name: str = 'index.html'
 
