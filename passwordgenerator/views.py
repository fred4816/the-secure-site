from django.views.generic import TemplateView


class PasswordGeneratorView(TemplateView):
    template_name = 'passwordgenerator.html'

