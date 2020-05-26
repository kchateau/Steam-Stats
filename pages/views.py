from django.views.generic import TemplateView
from lib.steam_api_calls.get_player_summaries import get_player_summaries
from lib.steam_api_calls.get_friend_list import get_friend_list
from lib.steam_api_calls.get_owned_games import get_owned_games



class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'on_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        steam_user = get_player_summaries(self.request.user.steam_id)
        context["steam_user"] = steam_user
        friend_list = get_friend_list(self.request.user.steam_id)
        context["friend_list"] = friend_list
        game_list = get_owned_games(self.request.user.steam_id)
        context["game_list"] = game_list
        return context    

class FriendsView(TemplateView):
    template_name = 'friends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friend_list = get_friend_list(self.request.user.steam_id)
        context["friend_list"] = friend_list
        return context
    