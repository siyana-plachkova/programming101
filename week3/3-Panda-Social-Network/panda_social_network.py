import re
import json


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class Panda:

    def __init__(self, name, email, gender):
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(email, str):
            raise TypeError

        if not isinstance(gender, str):
            raise TypeError

        if not self.__validate_email__(email):
            raise ValueError

        self.name = name
        self.email = email
        self.gender = gender

    def __validate_email__(self, email):
        return bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email))

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def isMale(self):
        return self.gender == "male"

    def isFemale(self):
        return self.gender == "female"

    def __str__(self):
        return "name: " + self.name + " email: " + self.email + " gender: " + self.gender

    def __eq__(self, other_panda):
        equal_names = self.name == other_panda.name
        equal_mails = self.email == other_panda.email
        equal_genders = self.gender == other_panda.gender

        return equal_names and equal_mails and equal_genders

    def __hash__(self):
        return hash(self.email)


class SocialNetwork:

    def __init__(self):
        self.relationships = {}

    def add_panda(self, panda):
        if panda not in self.relationships.keys():
            self.relationships[panda] = []
        else:
            raise PandaAlreadyThere("The panda already exists in the network")

    def has_panda(self, panda):
        if panda in self.relationships.keys():
            return True
        else:
            return False

    def are_friends(self, panda1, panda2):
        return panda2 in self.relationships[panda1] and panda1 in self.relationships[panda2]

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends("These two pandas are already friends.")

        self.relationships[panda1].append(panda2)
        self.relationships[panda2].append(panda1)

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False

        return self.relationships[panda]

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        visited = [panda1]
        queue = [panda1]
        path = {panda1: None}
        found = False

        while len(queue) != 0:
            curr_panda = queue.pop(0)
            if curr_panda == panda2:
                found = True
                break

            for friend in self.relationships[curr_panda]:
                if friend not in visited:
                    visited.append(friend)
                    queue.append(friend)
                    path[friend] = curr_panda

        path_len = 0
        if found:
            end = panda2
            while path[end] is not None:
                path_len += 1
                end = path[end]
        else:
            return -1

        return path_len

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) > 0

    def how_many_gender_in_network(self, level, panda, gender):
        if not self.has_panda(panda):
            return False

        gender_count = 0
        counted_friends = []
        level_friends = self.relationships[panda]
        while level != 0:
            if len(level_friends) == 0:
                break

            for p in level_friends:
                if p.gender == gender and p not in counted_friends:
                    gender_count += 1
                    counted_friends.append(p)

            level -= 1
            if level != 0:
                new_level_friends = []
                for p in level_friends:
                    new_level_friends += self.friends_of(p)
                level_friends = new_level_friends

        return gender_count

    def save(self, file_name):
        with open(file_name, 'w') as save_file:
            pandas = {}
            new_relationships = {}

            for panda in self.relationships.keys():
                panda_hash = str(hash(panda))
                pandas[panda_hash] = {
                    'name': panda.get_name(),
                    'email': panda.get_email(),
                    'gender': panda.get_gender()
                }
                new_relationships[panda_hash] = [str(hash(p)) for p in self.relationships[panda]]

            output = {
                'pandas': pandas,
                'relationships': new_relationships
            }

            json.dump(output, save_file)

    def load(self, file_name):
        with open(file_name, 'r') as load_file:
            input_object = json.load(load_file)
            pandas = input_object['pandas']
            relationships = input_object['relationships']

            for panda_hash in relationships.keys():
                panda_data = pandas[panda_hash]
                new_panda = Panda(panda_data['name'], panda_data['email'], panda_data['gender'])
                if not self.has_panda(new_panda):
                    self.add_panda(new_panda)

                for friend_hash in relationships[panda_hash]:
                    friend_data = pandas[friend_hash]
                    new_friend = Panda(friend_data['name'], friend_data['email'], friend_data['gender'])

                    if not self.are_friends(new_panda, new_friend):
                        self.make_friends(new_panda, new_friend)
