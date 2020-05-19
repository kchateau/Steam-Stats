from django.views.generic import TemplateView
from steam.webapi import WebAPI
import os


class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'on_login.html'

    def get_state(self, stateNum):
        if stateNum == 0:
            return "Offline"
        elif stateNum == 1:
            return "Online"
        elif stateNum == 2:
            return "Busy"
        elif stateNum == 3:
            return "Away"
        elif stateNum == 4:
            return "Snooze"
        elif stateNum == 5:
            return "Looking to Trade"
        elif stateNum == 6:
            return "Looking to Play"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api = WebAPI(os.environ.get("STEAM_KEY"))
        response = api.call('ISteamUser.GetPlayerSummaries', steamids=self.request.user.steam_id)
        state = self.get_state(response["response"]["players"][0]["profilestate"])
        response["response"]["players"][0]["profilestate"] = state
        context["response"] = response["response"]["players"][0]
        return context

    