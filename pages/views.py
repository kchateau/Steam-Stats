from django.views.generic import TemplateView
from lib.steam_api_calls.get_player_summaries import get_player_summaries

class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'on_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        steam_user = get_player_summaries(self.request.user.steam_id)
        context["steam_user"] = steam_user
        return context    