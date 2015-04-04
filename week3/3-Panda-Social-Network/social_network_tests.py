import unittest
import os
from panda_social_network import PandaAlreadyThere
from panda_social_network import Panda
from panda_social_network import SocialNetwork
from panda_social_network import PandasAlreadyFriends


class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network = SocialNetwork()
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.rado = Panda("Rado", "rado@pandamail.com", "male")
        self.tony = Panda("Tony", "tony@pandamail.com", "female")

        for panda in [self.ivo, self.rado, self.tony]:
            self.network.add_panda(panda)

    def test_init(self):
        self.assertTrue(isinstance(self.network, SocialNetwork))

    def test_add_panda(self):
        new_panda = Panda("Toshko", "toshko@pandamail.com", "male")
        self.network.add_panda(new_panda)
        self.assertIn(new_panda, self.network.relationships.keys())

        with self.assertRaises(PandaAlreadyThere):
            false_new_panda = Panda("Ivo", "ivo@pandamail.com", "male")
            self.network.add_panda(false_new_panda)

    def test_has_panda(self):
        search_for_panda = Panda("Rado", "rado@pandamail.com", "male")
        false_search_for_panda = Panda("Toshko", "toshko@pandamail.com", "male")
        self.assertTrue(self.network.has_panda(search_for_panda))
        self.assertFalse(self.network.has_panda(false_search_for_panda))

    def test_make_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        friends = self.network.relationships[self.rado].count(self.ivo) == 1 and self.network.relationships[self.ivo].count(self.rado) == 1
        self.assertTrue(friends)

        with self.assertRaises(PandasAlreadyFriends):
            self.network.make_friends(self.ivo, self.rado)

    def test_friends_of(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertIn(self.rado, self.network.friends_of(self.ivo))

    def test_connection_level(self):
        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.rado, self.tony)

        self.assertEqual(self.network.connection_level(self.ivo, self.rado), 1)
        self.assertEqual(self.network.connection_level(self.ivo, self.tony), 2)

    def test_are_connected(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.are_connected(self.ivo, self.rado))
        self.assertFalse(self.network.are_connected(self.ivo, self.tony))

        self.network.make_friends(self.rado, self.tony)
        self.assertTrue(self.network.are_connected(self.ivo, self.tony))

    def test_how_many_gender_in_network(self):
        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.rado, self.tony)
        toshko = Panda("Toshko", "toshko@pandamail.com", "male")
        self.network.make_friends(self.rado, toshko)

        self.assertEqual(self.network.how_many_gender_in_network(1, self.ivo, "male"), 1)
        self.assertEqual(self.network.how_many_gender_in_network(2, self.ivo, "male"), 3)
        self.assertEqual(self.network.how_many_gender_in_network(1, self.ivo, "female"), 0)
        self.assertEqual(self.network.how_many_gender_in_network(2, self.ivo, "female"), 1)

    def test_save_load(self):
        filename = "network.json"

        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.rado, self.tony)
        self.network.save(filename)

        new_network = SocialNetwork()
        new_network.load(filename)

        self.assertTrue(new_network.are_connected(self.ivo, self.rado))
        self.assertTrue(new_network.are_connected(self.ivo, self.tony))

        os.unlink(filename)

if __name__ == '__main__':
    unittest.main()
