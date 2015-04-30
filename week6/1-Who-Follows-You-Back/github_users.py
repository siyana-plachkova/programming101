import requests
import json
from graph import DirectedGraph


class GithubUsers:

    def __init__(self, username):
        self._users_graph = DirectedGraph()
        self._root_user = self._get_root_user(username)
        print(self._root_user)
        self._fill_graph(self._root_user)

    def _get_root_user(self, username):
        root_user = requests.get('https://api.github.com/users/' + username)
        return json.loads(root_user.text)

    def _fill_graph(self, user_obj, limit=0):
        if limit == 2 or 'login' not in user_obj:
            return

        if 'followers_url' in user_obj:
            followers_json = requests.get(user_obj['followers_url'])
            followers = json.loads(followers_json.text)
        else:
            followers = []

        if 'following_url' in user_obj:
            following_json = requests.get(user_obj['following_url'])
            following = json.loads(following_json.text)
        else:
            following = []

        for user in followers:
            if isinstance(user, dict):
                self._users_graph.add_edge(user['login'], user_obj['login'])
                self._fill_graph(user, limit + 1)

        for user in following:
            if isinstance(user, dict):
                self._users_graph.add_edge(user_obj['login'], user['login'])
                self._fill_graph(user, limit + 1)

    def do_you_follow(self, user):
        return user in self._users_graph.get_neighbours_from(self._root_user['login'])

    def do_you_follow_indirectly(self, user):
        my_follows = self._users_graph.get_neighbours_from(self._root_user['login'])
        their_follows = []

        for usr in my_follows:
            their_follows += self._users_graph.get_neighbours_from(usr)

        if user in their_follows:
            return True

        return False

    def does_he_she_follows(self, user):
        return self._root_user in self._users_graph.get_neighbours_from(user)

    def who_follows_you_back(self):
        my_followers = self._users_graph.get_starting_nodes(self._root_user['login'])

        follow_me_back = []

        for follower in my_followers:
            if self.do_you_follow(follower) or self.do_you_follow_indirectly(follower):
                follow_me_back.append(follower)

        return follow_me_back
