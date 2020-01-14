from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'on_login.html'
