from django.views.generic import TemplateView
from steam.webapi import WebAPI
import os


class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'on_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api = WebAPI(os.environ.get("STEAM_KEY"))
        response = api.call('ISteamUser.GetPlayerSummaries', steamids=self.request.user.steam_id)
        context["response"] = response["response"]["players"][0]
        return context
